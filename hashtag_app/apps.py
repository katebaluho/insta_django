from django.apps import AppConfig


class HashtagAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hashtag_app'

    def ready(self):
        from . import signals
        super().ready()
