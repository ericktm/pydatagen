from django import forms

from app.models import Project, Table, Field, TYPE_CHOICES, TableFile


class FormProject(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'required': ''
    }))

    class Meta:
        model = Project


class FormTable(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all(),
                                     widget=forms.HiddenInput)
    name = forms.CharField(widget=forms.TextInput(attrs={
        'required': ''
    }))

    class Meta:
        model = Table


class FormField(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'required': ''
    }))
    table = forms.ModelChoiceField(queryset=Table.objects.all(),
                                   widget=forms.HiddenInput)
    type = forms.ChoiceField(choices=TYPE_CHOICES, required=True)
    to_field = forms.ModelChoiceField(queryset=Field.objects.filter(active=True), label='Campo Origem', required=False)
    options = forms.CharField(widget=forms.Textarea(attrs={
        'cols': '50'
    }), required=False)


    class Meta:
        model = Field


class FormTableFile(forms.ModelForm):
    readonly_fields = ('table',)

    class Meta:
        model = TableFile

