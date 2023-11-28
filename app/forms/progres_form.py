from django.forms import ModelForm
from app.models import Progres

class ProgresForm(ModelForm):
    class Meta:
        model = Progres
        field = '__all__'