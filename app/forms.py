from django.forms.models import ModelForm
from app.models import Conection, Table


class ModelConection(ModelForm):
    class Meta:
        model = Conection

class FormTable(ModelForm):
    class Meta:
        model = Table