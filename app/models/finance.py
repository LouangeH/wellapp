from django.db import models
from models.cooperative import Cooperative

class Finance(models.Model):
    cooperative = models.ForeignKey(Cooperative, on_delete=models.CASCADE)
    nom_bank = models.CharField(max_length=45, null=True)
    numero_compte = models.CharField(max_length=100, null=True)
    somme = models.FloatField()

    def __str__(self) -> str:
        return self.nom_bank

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['cooperative','nom_bank','numero_compte'],
                name = 'compte_unique'
            )
        ]