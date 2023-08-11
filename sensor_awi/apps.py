from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = 'sensor_awi'
    label = 'sensor_awi'
    verbose_name = 'Sensor AWI API Plugin'

    def ready(self):
        from . import handlers
