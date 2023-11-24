from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=45, null=True)

    def __str__(self) -> str:
        return self.nom
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['nom'],
                name = 'unique_categorie_actif'
            )
        ]