import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # use websocket configuration
        await self.accept()
        await self.send(text_data=json.dumps({"message":"connection established"}))

    async def receive(self, text_data):
        data  = json.loads(text_data)
        message = data.get("message", "")
         # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "response": message
        }))

    async def disconnect(self, close_code):
        print("Disconnected")