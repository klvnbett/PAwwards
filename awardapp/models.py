from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.dispatch import receiver
# Create your models here.


class Projects(models.Model):
    '''
    this is the class to generate the user's projects
    '''
    project_name = models.CharField(max_length=300)
    image = CloudinaryField('images')
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE, blank=True)
    author_photo = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True, default='1')
    url = models.URLField()
    
    def save_project(self):
         self.save()

class Profile(models.Model):
    '''
    this is a class to generate the user's profile
    '''
    profile=models.ImageField(upload_to='profile')
    bio= models.TextField(blank=True)
    user_id=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    add_info=models.TextField(blank=False,null=True)
    