from django.forms import ModelForm
from app.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        field = '__all__'