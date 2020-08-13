from django.db import models
from django.contrib.auth import get_user_model

User =  get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User)
    profile_image = models.ImageField(upload_to = 'profiles/')
