from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

User =  get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to = 'profiles/')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Post.objects.create(user = instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    instance.post.save()


class Post(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    post_image = models.ImageField(upload_to = 'posts/')
    post_description = models.CharField(max_length=200)
    upload_date = models.DateField(auto_now_add=True)
    