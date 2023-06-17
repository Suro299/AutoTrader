from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("id", "username", "is_staff", "is_active", "money")
    list_filter = ("username", "money", "is_staff", "is_active")
    
    fieldsets = (
        ("Basic Information", {"fields": ("username", "cars", "details", "money", "avatar")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "date_created")}),
    )
    

    
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "password1", "password2", "is_staff",
                "is_active",
            )}
        ),
    )
    
    search_fields = ("id", "username")
    ordering = ("username", "is_staff")


admin.site.register(CustomUser, CustomUserAdmin)
