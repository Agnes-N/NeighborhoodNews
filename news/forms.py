from django import forms
from .models import Profile,Neighborhood,Business
from django.forms import ModelForm,Textarea,IntegerField

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class NewNeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ['user','occupants']

class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user','neighborhood']