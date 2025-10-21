from django import forms
from .models import Farmer

class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['name', 'farm', 'gender', 'is_contracted']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter farmer name'
            }),
            'farm': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the farm name'
            }),
            'gender': forms.RadioSelect(attrs={
                'class': 'form-check-input',
            }),
            'is_contracted': forms.Select(attrs={
                'class': 'form-control',
            }),
        }
