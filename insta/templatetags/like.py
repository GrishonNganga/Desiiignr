from django import template
from django.contrib.auth import get_user_model
import random

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

@register.simple_tag
def liked_by(post_id):
    likes = Like.objects.filter(post = post_id)
    number_guess_range = len(likes)
    if number_guess_range == 0:
        return None
    elif number_guess_range == 1:
        return likes[0].username
    else:
        selected_no = random.randint(0, number_guess_range -1)
        print(selected_no)
        return likes[selected_no].username
        

@register.simple_tag
def others(post_id):
    return len(Like.objects.filter(post = post_id)) -1