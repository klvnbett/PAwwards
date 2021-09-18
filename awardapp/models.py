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

class Profile(models.Model):
    '''
    this is a class to generate the user's profile
    '''
    