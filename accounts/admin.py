from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group

from .models import User

class UserAdmin(BaseUserAdmin):
    list_display = ("username", "is_staff")
    list_filter = ("is_staff",)
    search_fields = ("username",)

    fieldsets = (
        (_("Credentials"), {"fields": ("username", "password")}),
        (_("Permissions"),{"fields": ("is_staff",),}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)