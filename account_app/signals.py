from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from .models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, *args, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()