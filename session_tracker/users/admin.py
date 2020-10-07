from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

admin.autodiscover()


@admin.register(User)
class UserAdmin(UserAdmin):
    pass
