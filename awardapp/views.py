from django.shortcuts import render,redirect
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

            return redirect('index')

    else:
        form = NewProjectForm()
    return render(request,'awards/new_project.html',{'form':form})

def search_results(request):

    if 'project' in request.GET and request.GET['project']:
        search_term = request.GET.get('project')
        searched_projects = Projects.search_project(search_term)
        message = f'{search_term}'

        return render(request,'awards/search.html',{'message':message,'project':searched_projects})

    else:
        message = 'Kindly Enter a search Value'
        return render(request,'awards/search.html',{'message':message})