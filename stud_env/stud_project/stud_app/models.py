from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pass
  
class student(models.Model):
   
    class Months(models.TextChoices):
        Jan ='January'
        Feb ='February'
        March ='March'
        April ='April'
        May ='May'
        Jun ='June'
        July='July'
        Aug='August'
        Sup='September'
        oct='October'
        nov='November'
        dec='December'
    
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    marks = models.PositiveIntegerField()
    Exam_month = models.CharField(max_length=20,choices=Months.choices)
   
    def __str__(self):
        return self.name
     
    class Meta:
        db_table = 'stud_app_student'