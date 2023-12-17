from django.apps import AppConfig


class StatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sic'
    verbose_name = "Статистика"
    def ready(self):
        import sic.signals
