from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

from media_app.models import Media


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, related_name="profile")
    avatar = models.ImageField(default='default.jpg')
    phone = models.CharField(
                            max_length=16,
                            validators=(
                                RegexValidator(regex=r"^\+?\d{8,15}$", message="Неверный телефонный номер"),
                            ),
                            blank=True,
                            null=True
    )
    bio = models.TextField(null=True, blank=True)
    github = models.URLField(max_length=2048, null=True, blank=True)

    def __str__(self):
        return f'for user {self.user.username}'