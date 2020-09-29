# for routing our requests
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat import routing as chat_routing

# this will handle everything that passes through the server.
# by default it will redirect anything http to urls.py
# below is setting up for incoming websockets
application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat_routing.websocket_urlpatterns
        )
    )

})
