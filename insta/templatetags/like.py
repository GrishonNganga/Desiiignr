from django import template
from django.contrib.auth import get_user_model

User = get_user_model()

from ..models import Like, Post

register = template.Library()

@register.simple_tag
def check_like(post_id, user_id):
    user = User.objects.get(id =user_id)
    likes = Like.objects.filter(post = post_id).filter(username=user.username)
    print(likes)
    if len(likes) == 0:
        return False
    else:
        return True