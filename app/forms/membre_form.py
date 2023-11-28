from django.forms import ModelForm
from app.models import Membre

class MembreForm(ModelForm):
    class Meta:
        model = Membre
        field = '__all__'