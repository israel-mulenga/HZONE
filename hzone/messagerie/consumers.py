from channels.generic.websocket import AsyncWebsocketConsumer
import json
from django.contrib.auth import get_user_model
from .models import Message, Discussion
from channels.db import database_sync_to_async

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.discussion_id = self.scope['url_route']['kwargs']['discussion_id']
        self.room_group_name = f"chat_{self.discussion_id}"

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    @database_sync_to_async
    def get_sender(self, username):
        return User.objects.get(username=username)

    @database_sync_to_async
    def get_discussion(self, discussion_id):
        return Discussion.objects.get(id=discussion_id)

    @database_sync_to_async
    def create_message(self, discussion, sender, message_content):
        message = Message.objects.create(
            discussion=discussion,
            sender=sender,
            receiver=discussion.owner if sender == discussion.client else discussion.client,
            content=message_content
        )
        print(f"✅ Message enregistré : {message}")
        return message

    async def receive(self, text_data):
        data = json.loads(text_data)

        sender = await self.get_sender(data['sender'])
        discussion = await self.get_discussion(self.discussion_id)
        message = await self.create_message(discussion, sender, data['message'])

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message.content,
                'sender': sender.username,
                'timestamp': str(message.timestamp)
            }
        )

    async def chat_message(self, event):
        event["receiver"] = await self.get_receiver(event["sender"])
        print(f"✅ WebSocket message reçu : {event}")
        await self.send(text_data=json.dumps(event))

    @database_sync_to_async
    def get_receiver(self, sender_username):
        sender = User.objects.get(username=sender_username)
        discussion = Discussion.objects.get(id=self.discussion_id)
        return discussion.owner.username if sender == discussion.client else discussion.client.username  # ✅ Détermine le destinataire
