from django import forms
from django.forms.models import ModelForm

from app.models import Project, Table, Field, ForeignKey


class FormProject(ModelForm):
    class Meta:
        model = Project


class FormTable(ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all(),
                                     widget=forms.HiddenInput)

    class Meta:
        model = Table


class FormField(ModelForm):
    class Meta:
        model = Field
        exclude = {'table'}


class FormAssociate(ModelForm):
    class Meta:
        model = ForeignKey