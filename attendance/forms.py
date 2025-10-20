from django import forms
from .models import Attendance,Farmer

class FarmerForm(forms.ModelForm):
    class Meta:
        model=Farmer
        fields = ['name', 'farm']

        widgets = {

            'name':forms.TextInput(attrs={
                'class':'form-contrl',
                'placeholder':'Enter farmer name'
            }),

            'farm':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'enter the farm name'
            }),

        }