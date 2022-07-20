from django.urls import path
from .views import *
urlpatterns=[
   path('',home, name='home'),
#    path('stud-chart/',marks_chart, name='stud-chart'),
   path('stud-chart/',marks_chart.as_view(),name='stud-chart'),
]