from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Livro

class CustomUserAdmin(UserAdmin):
    pass

admin.site.register(User, CustomUserAdmin)
admin.site.register(Livro)

