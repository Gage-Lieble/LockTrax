from django import forms
from django.forms import ModelForm
from .models import *

class NameSearchForm(forms.ModelForm):
    
    class Meta:
        model = NameSearch
        fields = '__all__'
        