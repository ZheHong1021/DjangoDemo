"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# 【Default】
#region
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.django.base')

# application = get_asgi_application()
#endregion


# 【channels】
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from orders.routing import websocket_urlpatterns
application = ProtocolTypeRouter({
    # http請求
    "http": get_asgi_application(),


    # websocket請求
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})

