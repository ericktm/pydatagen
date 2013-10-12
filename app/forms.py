from django import forms
from django.forms.models import ModelForm
from django.forms.widgets import HiddenInput
from app.models import Project, Table


class FormProject(ModelForm):
    class Meta:
        model = Project


class FormTable(ModelForm):
    class Meta:
        model = Table
        exclude = {'project'}
