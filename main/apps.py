from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'


    # Fires up the signals file when a user instance is initiated
    def ready(self):
        import main.signals