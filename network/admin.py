from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Post, Relationship

# Registering models for Django admin functionality
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Relationship)