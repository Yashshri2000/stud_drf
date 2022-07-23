from django.urls import path,include

from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'view', viewStudent)


urlpatterns=[
   path('',home, name='home'),
   path('add/',add_stud, name='add'),
   path('stud-chart/',marks_chart.as_view(),name='stud-chart'),
   path('stud_view/',view_stud),
   path('api/', include(router.urls)),
]