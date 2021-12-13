from django.db import models
from django.core.validators import MaxValueValidator


class Menu(models.Model):
    menu_label = models.CharField(max_length=255, null=False, blank=False, unique=True)

    def __str__(self):
        return f"{self.id}: {self.menu_label}"


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, blank=False, null=False, on_delete=models.CASCADE, related_name='links')
    title = models.CharField(max_length=32, null=False, blank=False)
    url = models.CharField(max_length=256, null=False, blank=False)
    icon = models.ImageField(null=True, blank=True)
    priority = models.SmallIntegerField(validators=[MaxValueValidator(100)], default=0)

    class Meta:
        indexes = [
            models.Index(fields=['url', "menu"]),
            models.Index(fields=['menu'])
        ]
        unique_together = [("menu", "title"), ]

    def __str__(self):
        return f"{self.id}: {self.title}"