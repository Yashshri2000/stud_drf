from django import forms


class StudentForm(forms.Form):
    Months= (
        (1,'Jan'),(2,'Feb'),
        (3,'March'),(4,'April'),
        (5,'May'),(6,'Jun'),
        (7,'July'),(8,'Aug'),
        (9,'Sep'),(10,'Oct'),
        (11,'Nov'),(12,'Dec'),
    )
    name = forms.CharField(max_length=30)
    marks = forms.IntegerField()
    Exam_month = forms.ChoiceField(choices=Months)