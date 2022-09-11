from django import forms
from .models import Thumb
from django.forms import ModelForm
from .models import *
 
class GeeksForm(forms.ModelForm):
    

     class Meta:
            model=Thumb
            
            fields = ['img']  


# class UserForm(ModelForm):
#     class Meta:
#         model = Thumb
#         fields = ['img']

# from django import forms

# class UserForm(forms.Form):
    
#     img = forms.FileField()        