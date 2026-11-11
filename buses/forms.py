from django import forms
from .models import ALLBuses

class BusCreationForm(forms.ModelForm):
    class Meta:
        model = ALLBuses
        exclude = ['vendor']
