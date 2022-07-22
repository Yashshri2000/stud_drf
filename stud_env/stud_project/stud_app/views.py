from audioop import avg
from multiprocessing import context
from django.shortcuts import render
from django.db.models import Sum,Avg
from django.http import HttpResponse, JsonResponse
from .models import student
from .forms import *

from django.views.generic import View
   
from rest_framework.views import APIView
from rest_framework.response import Response
 
def home(request):
    if request.method == 'GET':
        context = {'form':StudentForm()}
        return render(request, 'home.html',context)
    
def add_stud(request):
    if request.method == 'GET':
        context = {'form':StudentForm()}
        return render(request, 'addStud.html',context)
    elif request.method == 'POST':
        form = StudentForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponse('Succefully Added!')
        context ={'form': form}
        return render(request,'addStud.html', context)
 
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
    
class marks_chart(APIView):
    authentication_classes = []
    permission_classes = []
 
   
    def get(self, request, format = None):
        labels = []
        data = []

        queryset = student.objects.values('Exam_month').annotate(marks=Avg('marks')).order_by('-marks') 
        for entry in queryset:
            labels.append(entry['Exam_month'])
            data.append(entry['marks'])
     
        return JsonResponse(data={
            'labels': labels,
            'data': data,
        })
    
