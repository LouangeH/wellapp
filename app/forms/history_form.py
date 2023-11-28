from django.forms import ModelForm
from app.models import History_Finance

class History_FinanceForm(ModelForm):
    class Meta:
        model = History_Finance
        field = '__all__'