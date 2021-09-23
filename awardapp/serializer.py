from rest_framework import serializers
from .models import *


class ProfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user','pic','bio','info']

class ProjSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['title','description','link','image']