from django.contrib.auth.models import User
from django.db import models

from hashtag_app.models import Hashtag


class Follower(models.Model):
    follower = models.ForeignKey(User, on_delete= models.CASCADE, related_name='followings', null=False, blank=False) #'последователь'
    following = models.ForeignKey(User, on_delete= models.CASCADE, related_name='followers', null=False, blank=False) #подписчики
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('follower', 'following'), )
        ordering = ['-create_date']

    def __str__(self):
        return f'follower{self.follower} to following {self.following}'


class FollowingHashtag(models.Model):
    follower = models.ForeignKey(User, on_delete= models.CASCADE, related_name='follow_hashtags', null=False, blank=False) #'последователь'
    follow_hashtag = models.ForeignKey(Hashtag, on_delete= models.CASCADE, related_name='followers', null=False, blank=False) #подписчики
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('follower', 'follow_hashtag'), )
        ordering = ['-create_date']

    def __str__(self):
        return f'follower{self.follower} to following {self.follow_hashtag}'