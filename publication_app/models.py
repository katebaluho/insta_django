from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.shortcuts import redirect
from django.urls import reverse

from media_app.models import Media


class Post(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    title = models.CharField(max_length=256, unique=False, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='posts', null=True)
    file = models.ForeignKey(Media, on_delete=models.PROTECT, null=True, blank=True, related_name='posts')