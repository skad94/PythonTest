# Fichier modelisant les tables
from django.db import models

# Creation du "modele" de base de donne
# Une personne a un prenom, nom, ID, une equipe
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

## Une clé a un nom, un ID et peut être stocké a different lieu 
class Cle(models.Model):
    nom = models.CharField(max_length=100)
    identificat = models.IntegerField()

    # Liste deroulante du stockage des clés
    TYPE_CHOICES = [
        ('Salon', 'Salon'),
        ('Cuisine', 'Cuisine'),
        ('Tiroir', ' tiroir'),
    ]
    lieu = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES, # Liste des équipes
        default='ext'  # Option par défaut
    )

    def __str__(self):
        return f"{self.prenom} {self.nom}"

