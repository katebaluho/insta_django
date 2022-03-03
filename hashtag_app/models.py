
from django.db import models

from publication_app.models import Post


class Hashtag(models.Model):
    hashtag_label = models.CharField(max_length=30)
    posts = models.ManyToManyField(Post, blank=True, related_name='hashtags')



    def __str__(self):
        return f"{self.hashtag_label}"
