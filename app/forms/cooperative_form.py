from django.forms import ModelForm
from app.models import Cooperative

class CooperativeForm(ModelForm):
    class Meta:
        model = Cooperative
        field = '__all__'