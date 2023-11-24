from django.db import models
from models.cooperative import Cooperative

bnk = (
    ('C','Caisse Social'),
    ('B', 'Banque'),
    ('M', 'Micro-Finance')
)

class Project(models.Model):
    cooperative = models.ForeignKey(Cooperative, on_delete=models.CASCADE)
    nom_projet = models.CharField(max_length=45, null=True)
    budget = models.FloatField()
    periode_debut = models.DateField()
    source = models.CharField(max_length=1, choices=bnk, default="C")
    date_set = models.DateTimeField(auto_now_add=True)


    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['cooperative','nom_projet','periode_debut'],
                name = 'unique_project'
            )
        ]