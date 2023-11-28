from django.forms import ModelForm
from app.models import Actif

class ActifForm(ModelForm):
    class Meta:
        model = Actif
        fields = '__all__'