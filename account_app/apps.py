from django.apps import AppConfig


class AccountsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account_app'

    def ready(self):
        from . import signals
        super().ready()