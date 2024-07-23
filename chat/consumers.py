import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User
from .models import Message

class ChatRoomConsumer(AsyncWebsocketConsumer):
    online_users = set()

    async def connect(self):
        self.room_group_name = 'chat_main'
        self.username = self.scope['user'].username

        self.online_users.add(self.username)

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_list_update',
                'online_users': list(self.online_users)
            }
        )

    async def disconnect(self, code):
        self.online_users.remove(self.username)

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_list_update',
                'online_users': list(self.online_users)
            }
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await sync_to_async(Message.objects.create)(
            message=message,
            sender=self.scope['user']
        )

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chatroom_message',
                'message': message,
                'username': self.username,
            }
        )

    async def chatroom_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
        }))

    async def user_list_update(self, event):
        online_users = event['online_users']

        await self.send(text_data=json.dumps({
            'online_users': online_users
        }))



