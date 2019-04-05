from django import forms
from django.forms import models 
from .models import Class_name
from .models import Book

class Class_name_Form(models.ModelForm):
    class Meta:
        model=Class_name
        fields=['first_name','last_name','contact','email','password']


class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['title','author','pdf']
