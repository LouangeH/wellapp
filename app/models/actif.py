from django.db import models
from models.cooperative import Cooperative
from models.categorie import Categorie

et = (
    ('O','Operationnel'),
    ('P','En panne'),
    ('D', 'Defectueux')
)

class Actif(models.Model):
    cooperative = models.ForeignKey(Cooperative, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    etat = models.CharField(max_length=1, choices=et, default="")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['categorie','cooperative','quantite'],
                name = 'unique_actif'
            )
        ]