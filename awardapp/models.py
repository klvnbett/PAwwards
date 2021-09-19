from django.db import models
import datetime as dt
from django.contrib.auth.models import User
# Create your models here.


class Projects(models.Model):
    '''
    this is the class to generate the user's projects
    '''
    title=models.CharField(max_length=125)
    description=models.TextField
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Profile(models.Model):
    '''
    this is a class to generate the user's profile
    '''
    profile=models.ImageField(upload_to='profile')
    bio= models.TextField(blank=True)
    user_id=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    add_info=models.TextField(blank=False,null=True)
    