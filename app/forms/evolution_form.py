from django.forms import ModelForm
from app.models import Evolution

class EvolutionForm(ModelForm):
    class Meta:
        model = Evolution
        field = '__all__'