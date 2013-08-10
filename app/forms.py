from django.forms.models import ModelForm
from app.models import Conection

class ModelConection(ModelForm):
    class Meta:
        model = Conection