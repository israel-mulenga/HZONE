from django.core.asgi import get_asgi_application
from django.urls import re_path
from messagerie.consumers import ChatConsumer
from channels.routing import ProtocolTypeRouter, URLRouter

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter([
           re_path(r'ws/chat/(?P<discussion_id>\d+)/$', ChatConsumer.as_asgi()),  # ✅ Ajout de discussion_id
    ]),
})

# Note: The URL pattern for the WebSocket connection should match the one used in the JavaScript code.



websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<discussion_id>\d+)/$', ChatConsumer.as_asgi()),  # ✅ Ajout de discussion_id
]

