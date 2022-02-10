import re

from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from django.dispatch import receiver

from publication_app.models import Post
from .models import Hashtag


@receiver(post_save, sender=Post)
def find_or_create_tags(sender, instance, created, *args, **kwargs):
    pattern = re.compile(r'#(\w+)\s?')
    for tag in re.findall(pattern, instance.text):
        tag_instance, tag_is_created = Hashtag.objects.get_or_create(hashtag_label=tag)
        tag_instance.posts.add(instance)