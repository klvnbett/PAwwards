from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt 
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
def index(request):
    date=dt.date.today()
    projects = Projects.objects.all()
    return render (request,'awards/index.html',{"date":date, "projects":projects})
