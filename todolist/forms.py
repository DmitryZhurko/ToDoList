from django import forms
from django.forms import TextInput

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']

        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'введите задачу',
                'class': 'd-inline-block',
                'style': 'width: 400px; height:40px;'


            }),

        }


