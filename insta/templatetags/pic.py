from django import template

from django.contrib.auth import get_user_model
from ..models import Profile

User = get_user_model()


register = template.Library()

@register.simple_tag
def get_pic(username):
    user = User.objects.filter(username = username).first()
    profile = Profile.objects.filter(user = user).exists()
    if profile:
        return user.profile.profile_image.url
    else:
        return None
