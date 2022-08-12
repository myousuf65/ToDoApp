from django import forms
from .models import ToDoApp_model


class ToDoApp_form(forms.ModelForm):
    class Meta:
        model = ToDoApp_model
        fields = [
            'item'
        ]
        widgets = {
            'item' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please input here...'})
        }