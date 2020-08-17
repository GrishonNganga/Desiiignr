from django import template
from django.contrib.auth import get_user_model
import random

from ..models import Profile, Follower

User = get_user_model()

register = template.Library()

@register.simple_tag
def to_follow(user_id):
    user = User.objects.get(id = user_id)
    user_followers = Follower.objects.filter(user= user_id).exists()
    print(Follower.objects.filter(user= user_id))
    print(user_followers)
    if user_followers:
        user_followers = Follower.objects.filter(user= user).exists()
        users = User.objects.exclude(id = user_id).exclude(follower = user_followers)
    else:
        users = User.objects.exclude(id = user_id)
    print(users)
    follow_list = []
    random_ints = []
    for _ in range(4):
        user_no = random.randint(0, len(users)-1)
        if user_no not in random_ints:
            random_ints.append(user_no)
            follow_list.append(users[user_no])
            
    final_follow_list = []
    print(follow_list)
    for user in follow_list:
        print(user)
        if Profile.objects.filter(user = user.id).exists():
            data = {'username': user.username, 'user_id': user.id, 'profile': user.profile.profile_image.url}
            final_follow_list.append(data)
            print(final_follow_list)
        else:
            data = {'username': user.username, 'user_id': user.id, 'profile': None}
            final_follow_list.append(data)
    print(final_follow_list)

    return final_follow_list