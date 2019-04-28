DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'awx',
        'USER': 'awx',
        'PASSWORD': 'polo123polo',
        'HOST': 'postgres',
        'PORT': "31699",
    }
}
BROKER_URL = 'amqp://{}:{}@{}:{}/{}'.format(
    "mvne",
    "polo123polo",
    "rabbitmq-svc",
    "5672",
    "awx")
CHANNEL_LAYERS = {
    'default': {'BACKEND': 'asgi_amqp.AMQPChannelLayer',
                'ROUTING': 'awx.main.routing.channel_routing',
                'CONFIG': {'url': BROKER_URL}}
}

