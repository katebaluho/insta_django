from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from publication_app.models import Post


class Comment(models.Model):
    text = models.TextField(max_length=1024, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False, related_name='comments')

    def __str__(self):
        return f'{self.text}'

