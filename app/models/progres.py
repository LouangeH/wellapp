from django.db import models
from models.membre import Membre

ch = (
    ('Y', 'Oui'),
    ('N', 'Non')
)


class Progres(models.Model):
    nom = models.ForeignKey(Membre, on_delete=models.CASCADE)
    cam = models.CharField(max_length=1, choices= ch, default="N")
    agr = models.CharField(max_length=45, null=True)
    somme = models.IntegerField()
    vsla = models.CharField(max_length=1, choices=ch, default="N")
    
    
   
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['nom','agr','somme'],
                name = 'unique_progres'
            )
        ]