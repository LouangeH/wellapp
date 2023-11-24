from django.db import models
from models.cooperative import Cooperative

sexe = (
    ('M', 'Masculin'),
    ('F', 'Feminin')
)

cel = (
    ('S', 'Célibataire'),
    ('M', 'Marié(e)'),
    ('W', 'Veuf(ve)')
)

class Membre(models.Model):
    nom = models.CharField(max_length=45, null=True)
    prenom = models.CharField(max_length=45, null=True)
    date_naissance = models.IntegerField()
    genre = models.CharField(max_length=1, choices=sexe, default="M")
    marital = models.CharField(max_length=1, choices=cel, default="M")
    telephone = models.IntegerField()
    cooperative = models.ForeignKey(Cooperative, on_delete=models.CASCADE)
    
    # lors du choix le nom va s'affiche
    def __str__(self) -> str:
        return f"{self.nom} {self.prenom}"
    
    # ca nous permets de saisir le nom du membre de la cooperative une et une seule fois
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['nom','prenom','date_naissance','cooperative'],
                name = 'unique_membre'
            )
        ]