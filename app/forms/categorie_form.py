from django.forms import ModelForm
from app.models import Categorie

class CategorieForm(ModelForm):
    class Meta:
        model = Categorie
        field = '__all__'