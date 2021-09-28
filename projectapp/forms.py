from django import forms
from projectapp.models import UserProfile

class FormRegisterUser(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField(max_length=30, required=True)
    #profile_picture = forms.FileField()
    phone_number = forms.CharField(max_length=20, required=True)
    short_description = forms.CharField(max_length=150, required=True)
    
