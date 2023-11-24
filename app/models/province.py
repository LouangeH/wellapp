from django.db import models

class Province(models.Model):
    nom = models.CharField(max_length=45, null=True)

    def __str__(self) -> str:
        return self.nom
    
    # ca nous permets de saisir le nom du membre de la cooperative une et une seule fois
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['nom'],
                name = 'unique_province'
            )
        ]