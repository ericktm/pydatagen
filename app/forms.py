from django import forms

from app.models import Project, Table, Field, TYPE_CHOICES, TableFile


class FormProject(forms.ModelForm):
    name = forms.CharField(label='Nome do Projeto', widget=forms.TextInput(attrs={
        'required': ''
    }))

    def save(self, user, commit=True):
        project = super(FormProject, self).save(commit=False)
        project.user = user

        if commit:
            project.save()

        return project

    class Meta:
        model = Project
        fields = ('name',)


class FormTable(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all(),
                                     widget=forms.HiddenInput)
    name = forms.CharField(label='Nome', widget=forms.TextInput(attrs={
        'required': ''
    }))

    class Meta:
        model = Table
        fields = ('project', 'name')


class FormField(forms.ModelForm):
    name = forms.CharField(label='Nome:', widget=forms.TextInput(attrs={
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
        exclude = ('',)


class FormTableFile(forms.ModelForm):
    readonly_fields = ('table',)

    class Meta:
        model = TableFile
        exclude = ('',)

