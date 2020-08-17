from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

User =  get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to = 'profiles/')


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_image = models.ImageField(upload_to = 'posts/')
    post_description = models.CharField(max_length=200)
    upload_date = models.DateField(auto_now_add=True)

   
    @classmethod
    def get_all_posts(cls):
        return Post.objects.all()

    @classmethod
    def get_posts_for_user(cls, id):
        return list(Post.objects.filter(user = id))


class Follower(models.Model):
    username = models.CharField(max_length=100)
    user = models.ManyToManyField(User)


class Like(models.Model):
    username = models.CharField(max_length=100)
    post = models.ManyToManyField(Post)


class Comment(models.Model):
    username = models.CharField(max_length=100)
    post = models.ManyToManyField(Post)
    comment = models.CharField(max_length=250)