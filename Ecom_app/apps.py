from django.apps import AppConfig


class EcomAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Ecom_app'

    def ready(self):
        import Ecom_app.signals
