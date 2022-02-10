from django.contrib.auth.models import User
from django.db import models


class Media(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    file = models.ImageField(null=False, blank=False)