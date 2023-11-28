from django.forms import ModelForm
from app.models import Finance

class FinanceForm(ModelForm):
    class Meta:
        model = Finance
        field = '__all__'