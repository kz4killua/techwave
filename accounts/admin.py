# Importing necessary modules from Django
from django.contrib import admin  # For registering models to be managed via the admin site
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin  # Customizing user admin interface
from django.utils.translation import gettext_lazy as _  # For internationalization and translation
from django.contrib.auth.models import Group  # For managing user groups in the admin interface

from .models import User  # Importing the custom User model

# Custom admin class to modify how the User model is displayed in the admin interface
class UserAdmin(BaseUserAdmin):
    # Display the username and staff status in the list view
    list_display = ("username", "is_staff")
    
    # Filter options to filter by staff status
    list_filter = ("is_staff",)
    
    # Search functionality for the username field in the admin list view
    search_fields = ("username",)

    # Fieldsets define the sections and fields to display in the User edit form
    fieldsets = (
        (_("Credentials"), {"fields": ("username", "password")}),  # Fields related to credentials (username and password)
        (_("Permissions"), {"fields": ("is_staff",)}),  # Fields related to user permissions (e.g., is_staff)
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),  # Important dates like last login and account creation
    )

# Registering the custom User model with the custom UserAdmin interface
admin.site.register(User, UserAdmin)

# Unregistering the default Group model from the admin interface (no longer needed if you're not using groups)
admin.site.unregister(Group)
