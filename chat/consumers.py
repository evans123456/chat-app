from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
import time


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        async_to_sync(self.channel_layer.group_add)(  # take this function and convertit to a synchronous function
            "chat",
            self.channel_name

        )
        self.accept()

    def receive(self, text_data):
        async_to_sync(self.channel_layer.group_send)(  # take this function and convertit to a synchronous function
            "chat",
            {
                "type": "chat_message",
                "message": text_data
            }

        )
        # text_data_json = json.loads(text_data)
        # text_data_json['message'] += "..echo.."
        # while True:
        #     self.send(json.dumps(text_data_json))
        #     time.sleep(1)

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=message)

    def disconect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(  # take this function and convertit to a synchronous function
            "chat",
            self.channel_name

        )
