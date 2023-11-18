from django.contrib import admin
from djshop.auths.users.models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class DjshopUserAdmin(UserAdmin):
    list_display = ("username", "email", "verified_email", "first_name", "last_name", "is_staff")

