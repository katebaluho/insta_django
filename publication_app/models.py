from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    title = models.CharField(max_length=256, unique=False, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    image = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='posts', null=True)

