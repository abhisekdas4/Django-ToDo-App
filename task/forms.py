from django import forms
from django.forms import ModelForm
from .models import TaskModel


class TaskModelForm(ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'
