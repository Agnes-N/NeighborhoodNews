from django import forms
from .models import Profile
from django.forms import ModelForm,Textarea,IntegerField

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','projects']