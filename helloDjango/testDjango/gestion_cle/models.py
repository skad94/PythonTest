# Fichier modelisant les tables
from django.db import models

# Creation du "modele" de base de donne
# Un
class Person(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    identificat = models.IntegerField()

    # Liste deroulante des equipes
    #Possibilote d'ajouter un nom d'equipe ou de modifier le libellé
    TYPE_CHOICES = [
        ('CA', '''Conseil d'Administration'''),
        ('SONO', 'Musique et son'),
        ('ext', ' exterieures ou autres'),
    ]
    equipe = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES, # Liste des équipes
        default='ext'  # Option par défaut
    )

    def __str__(self):
        return f"{self.prenom} {self.nom}"

