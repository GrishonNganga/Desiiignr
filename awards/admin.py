from django.contrib import admin
from .models import Profile, Post, Rate, Comment

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Rate)
admin.site.register(Comment)