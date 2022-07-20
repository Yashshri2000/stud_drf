from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pass
  
class student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    marks = models.PositiveIntegerField()
   
    def __str__(self):
        return self.name
     
    class Meta:
        db_table = 'stud_app_student'