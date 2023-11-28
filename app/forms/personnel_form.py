from django.forms import ModelForm
from app.models import Personnel

class PersonnelForm(ModelForm):
    class Meta:
        model = Personnel
        field = '__all__'