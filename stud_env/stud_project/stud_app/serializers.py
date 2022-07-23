from dataclasses import fields
from rest_framework import serializers
from .models import *

class StudSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'