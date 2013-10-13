from django import forms
from django.forms.models import ModelForm
from django.forms.widgets import HiddenInput
from app.models import Project, Table, Field, ForeignKey


class FormProject(ModelForm):
    class Meta:
        model = Project

class FormTable(ModelForm):
    class Meta:
        model = Table
        exclude = {'project'}


class FormField(ModelForm):
    class Meta:
        model = Field
        exclude = {'table'}


class FormAssociate(ModelForm):
    class Meta:
        model = ForeignKey