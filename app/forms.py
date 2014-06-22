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
    table = forms.ModelChoiceField(queryset=Table.objects.all(),
                                   widget=forms.HiddenInput)
    to_field = forms.ModelChoiceField(queryset=Field.objects.filter(active=True), label='Campo Origem')

    class Meta:
        model = Field


class FormAssociate(ModelForm):
    class Meta:
        model = ForeignKey