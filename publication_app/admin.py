from django.contrib import admin

# Register your models here.
from publication_app.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', "create_date", 'title',)
    readonly_fields = ('create_date',)
