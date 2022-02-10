from django.contrib import admin

# Register your models here.
from .models import User
from django.contrib.auth.admin import UserAdmin as UserAdminBase
from account_app.models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile


admin.site.unregister(User)


@admin.register(User)
class UserAdmin(UserAdminBase):
    inlines = (
        ProfileInline,
    )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserAdmin, self).get_inline_instances(request, obj)