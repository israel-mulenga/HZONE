import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from asgiref.sync import sync_to_async  # ✅ Convertir les appels synchrones en asynchrones
from .models import Message

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        sender = self.scope["user"]
        receiver_username = self.scope["url_route"]["kwargs"]["receiver"]  # ✅ Récupère le destinataire depuis l'URL
        receiver = await sync_to_async(User.objects.get)(username=receiver_username)

        if sender.is_authenticated and receiver:
            self.room_group_name = f"chat_{min(sender.username, receiver.username)}_{max(sender.username, receiver.username)}"  # ✅ Room unique pour les deux utilisateurs
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            await self.accept()
            await self.send(text_data=json.dumps({"message": "connection established"}))
        else:
            await self.close()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        sender = self.scope["user"]
        receiver = await sync_to_async(User.objects.get)(username=data["receiver"])  # ✅ Convertir l’appel en async

        if sender.is_authenticated and receiver:
            message = await sync_to_async(Message.objects.create)(sender=sender, receiver=receiver, content=data["message"])  # ✅ Sauvegarde asynchrone
            
                # ✅ Diffusion du message uniquement au destinataire et à l'expéditeur
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "sender": sender.username,
                    "receiver": receiver.username,
                    "message": data["message"],
                    "timestamp": str(message.timestamp),
                },
            )
        else:
            await self.send(text_data=json.dumps({"error": "Utilisateur non authentifié ou destinataire introuvable"}))

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))
