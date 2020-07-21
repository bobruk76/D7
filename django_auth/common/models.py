from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):

    age = models.IntegerField()
    extra_data = models.TextField(default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
