from django import forms
from .models import Pacient, Tratament

class PacientForm(forms.ModelForm):
    class Meta:
        model = Pacient
        fields = '__all__'

class TratamentForm(forms.ModelForm):
    class Meta:
        model = Tratament
        fields = '__all__'
