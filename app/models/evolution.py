from django.db import models
from models.project import Project

class Evolution(models.Model):
    projet = models.ForeignKey(Project, on_delete=models.CASCADE)
    depense = models.FloatField()
    reste = models.FloatField()
    date_set = models.DateField(auto_now_add=True)