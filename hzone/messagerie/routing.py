from django.core.asgi import get_asgi_application
from django.urls import re_path
from messagerie.consumers import ChatConsumer
from channels.routing import ProtocolTypeRouter, URLRouter

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter([
        re_path(r"ws/chat/$", ChatConsumer.as_asgi()),  # ✅ Vérifie bien le `$` ici
    ]),
})

websocket_urlpatterns = [
    re_path(r"ws/chat/$", ChatConsumer.as_asgi()),
]