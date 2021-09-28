from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
import datetime   
    
class UserProfile(models.Model):
    #profile_picture = models.ImageField('img', upload_to='path/')
    phone_number = models.CharField(max_length=100)
    short_description = models.CharField(max_length=140)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
class AnonymousUser(models.Model):
    ip = models.GenericIPAddressField()
    created_date = models.DateTimeField()

    def __str__(self):
        return self.ip
    

class Room(models.Model):
    created_date = models.DateField()
    anonymousUser = models.ForeignKey('AnonymousUser', on_delete=models.CASCADE)
    speaker = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Speaker: {self.speaker.user.username}'
    