from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post

User = get_user_model()

class UsersSerialized(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class ProjectsSerialized(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'post_image', 'post_description', 'user', 'upload_date')