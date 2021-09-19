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

def comment(request,id):
    id = id
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.user = request.user
            project = Projects.objects.get(id = id)
            comment.project_id = project
            comment.save()
            return redirect('index')

        else:
            project_id = id
            messages.info(request,'Ensure all required fields are filled')
            return redirect('comment',id = project_id)

    else:
        id = id
        form = CommentForm()
        return render(request,'awards/comment.html',{'form':form,'id':id})