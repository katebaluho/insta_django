from django.contrib import admin

# Register your models here.
from media_app.models import Media


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    model = Media