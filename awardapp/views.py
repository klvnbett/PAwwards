from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    all_projects = Projects.all_projects()
    return render(request,'awards/index.html',{'all_projects':all_projects})
    
def profile(request):
    
    all_projects = Projects.objects.filter(user = request.user)
    return render(request,'awards/profile.html',{'all_projects':all_projects})

def new_project(request):
      if request.method=='POST':
        form = NewProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()