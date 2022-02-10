from django.contrib.auth.models import User
from django.db import models

from comments_app.models import Comment
from publication_app.models import Post


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=False, related_name='likes')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=False, related_name='likes')

    class Meta:
        unique_together = (('user', 'post'), ('user', 'comment'))