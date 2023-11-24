from django.db import models
from models.membre import Membre
from models.province import Province

vie = (
    ('Y', 'Oui'),
    ('N', 'Non')
)

etude = (
    ('N', 'Aucun'),
    ('P','Primaire'),
    ('S', 'Secondaire'),
    ('U', 'Universitaire')
)

class Personnel(models.Model):
    nom = models.ForeignKey(Membre, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    commune = models.CharField(max_length=45, null=True)
    zone = models.CharField(max_length=45, null=True)
    pere_vivant = models.CharField(max_length=1, choices=vie, default="Y")
    mere_vivant = models.CharField(max_length=1, choices=vie, default="Y")
    niv_etude = models.CharField(max_length=1, choices=etude, default="N")
    cni = models.CharField(max_length=100, null=True)
    lieu_deliv = models.CharField(max_length=45, null=True)
    
    # ca nous permets de saisir le nom du membre de la cooperative une et une seule fois
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['nom','cni'],
                name = 'unique_perso'
            )
        ]