from django import forms
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import *
class StudentForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('add')
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit','submit'))
    
    class Meta:
        model= student
        fields = ('name','marks','Exam_month')
  
        