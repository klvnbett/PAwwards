from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
from .forms import *
from rest_framework.views import APIView
from . serializer import *
from rest_framework.response import Response


# Create your views here.
@login_required(login_url = '/accounts/login/')
def index(request):
    if request.method=='POST':
        form=ProjectForm(request.POST)
        form=ProfileForm(request.POST)
        if form.is_valid():
            project=form.save(commit=False)
            project.user=request.user
            project.save()
    else:
        form=ProjectForm()
        form=ProfileForm()
    
    try:
        profiles=Profile.objects.all()
        projects=Projects.objects.all()
    
    except:
        Projects.DoesNotExist,
        profiles.DoesNotExist,
        
    # all_projects = Projects.all_projects()
    return render(request,'awards/index.html',{"profiles":profiles,"projects":projects,"form":form})

@login_required(login_url = '/accounts/login/')
def profile(request):

    all_projects = Projects.objects.filter(user = request.user)
    return render(request,'awards/profile.html',{'all_projects':all_projects })


@login_required(login_url = '/accounts/login/')
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


@login_required(login_url = '/accounts/login/')
def search_results(request):

    if 'project' in request.GET and request.GET['project']:
        search_term = request.GET.get('project')
        searched_projects = Projects.search_project(search_term)
        message = f'{search_term}'

        return render(request,'awards/search.html',{'message':message,'project':searched_projects})

    else:
        message = 'Kindly Enter a search Value'
        return render(request,'awards/search.html',{'message':message})


@login_required(login_url = '/accounts/login/')
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


@login_required(login_url = '/accounts/login/')
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')

    else:
        form = EditProfileForm(request.POST,request.FILES)
    return render(request,'awards/update_profile.html',{'form':form})


@login_required(login_url = '/accounts/login/')
def single_project(request,id):  

    project = Projects.objects.get(id = id)
    comments = Comments.objects.filter(project_id = id)
    rates = Ratings.objects.filter(project_id = id)
    designrate = []
    usabilityrate = []
    contentrate = []
    if rates:
        for rate in rates:
            designrate.append(rate.design)
            usabilityrate.append(rate.usability)
            contentrate.append(rate.content)

        total = len(designrate)*10
        design = round(sum(designrate)/total*100,1)
        usability = round(sum(usabilityrate)/total*100,1)
        content = round(sum(contentrate)/total*100,1)
        return render(request,'awards/single_project.html',{'project':project,'comments':comments,'design':design,'usability':usability,'content':usability})

    else:
        design = 0
        usability = 0
        content = 0       

        return render(request,'awards/single_project.html',{'project':project,'comments':comments,'design':design,'usability':usability,'content':usability})


@login_required(login_url = '/accounts/login/')
def rate(request,id):
    if request.method =='POST':
        rates = Ratings.objects.filter(id = id)
        for rate in rates:
            if rate.user == request.user:
                messages.info(request,'Rating is only done once')
                return redirect('singleproject',id)
        design = request.POST.get('design')
        usability = request.POST.get('usability')
        content = request.POST.get('content')

        if design and usability and content:
            project = Projects.objects.get(id = id)
            rate = Ratings(design = design,usability = usability,content = content,project_id = project,user = request.user)
            rate.save()
            return redirect('singleproject',id)

        else:
            messages.info(request,'Input all fields')
            return redirect('singleproject',id)


    else:
        messages.info(request,'Input all fields')
        return redirect('singleproject',id)

class ProjectApi(APIView):
    def get(self, request, format=None):
        all_projects = Projects.objects.all()
        serializers = ProjSerializer(all_projects, many=True)
        return Response(serializers.data)

class ProfileApi(APIView):
    def get(self, request, format=None):
        all_projects = Profile.objects.all()
        serializers = ProfSerializer(all_projects, many=True)
        return Response(serializers.data)
