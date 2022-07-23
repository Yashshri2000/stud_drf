from audioop import avg
from multiprocessing import context
from django.contrib import messages
from django.shortcuts import render
from django.db.models import Sum,Avg,Func
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializers import StudSerializer
from .models import student
from .forms import *

from django.views.generic import View
   
from rest_framework.views import APIView
from rest_framework.response import Response
 
def home(request):
    if request.method == 'GET':
        context = {'form':StudentForm()}
        return render(request, 'home.html',context)

def view_stud(request):
    return render(request,'viewStud.html')

    
def add_stud(request):
    if request.method == 'GET':
        context = {'form':StudentForm()}
        return render(request, 'addStud.html',context)
    elif request.method == 'POST':
        form = StudentForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            form = StudentForm()
            messages.success(request,"student added successfully!")           
        return render(request,'addStud.html', {'form':form})
 
# def marks_chart(request):
#     labels = []
#     data = []
 
#     queryset = student.objects.values('name').annotate(marks=Sum('marks')).order_by('-marks') 
#     for entry in queryset:
#         labels.append(entry['name'])
#         data.append(entry['marks'])
     
#     return JsonResponse(data={
#         'labels': labels,
#         'data': data,
#     })

class Round(Func):
    function = 'ROUND'
    template= '%(function)s(%(expressions)s,2)'
    
class marks_chart(APIView):
    authentication_classes = []
    permission_classes = []
 
   
    def get(self, request, format = None):
        labels = []
        data = []

        queryset = student.objects.values('Exam_month').annotate(marks=(Round(Avg('marks')))).order_by('-marks') 
        for entry in queryset:
            labels.append(entry['Exam_month'])
            data.append(entry['marks'])
     
        return JsonResponse(data={
            'labels': labels,
            'data': data,
        })
    
# @api_view(['GET'])
# def viewStudent(request):
#     queryset = student.objects.all()
#     serializer = StudSerializer(queryset, many=True)
#     ctx = {'data':serializer.data}
#     return render(request, 'viewStud.html',ctx)

class viewStudent(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = StudSerializer
    
    
