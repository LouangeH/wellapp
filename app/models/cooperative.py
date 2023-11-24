from django.db import models

class Cooperative(models.Model):
    nom_cooperative = models.CharField(max_length=45, null=True)
    localite = models.CharField(max_length=45, null=True)
    nif = models.IntegerField() # le NIF (Numero d'Immatriculation Fiscale)
    rc = models.CharField(max_length=45, null=True) # le RC (Registre de Commerce)
    
    # lors du choix le nom va s'affiche
    def __str__(self) -> str:
        return self.nom_cooperative
    
    # ca nous permets de saisir la cooperative plus d'une fois
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['nom_cooperative','nif','rc'],
                name = 'unique_cooperative'
            )
        ]