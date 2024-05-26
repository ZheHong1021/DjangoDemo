# channels for websocket

ASGI_APPLICATION = 'config.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        # Local Test
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
         
        # # Redis
        # "BACKEND": "channels_redis.core.RedisChannelLayer",
        # "CONFIG": {
        #     "hosts": [("127.0.0.1", 6379)],
        #     #或"hosts": [os.environ.get('REDIS_URL', 'redis://127.0.0.1:6379/1')],
        #  },
    },

}