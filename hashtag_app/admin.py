from django.contrib import admin

# Register your models here.
from hashtag_app.models import Hashtag


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    model = Hashtag