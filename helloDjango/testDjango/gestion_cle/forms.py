# Fichier pour le formulaire et faire une interface Utilisateur simple
# 
from django import forms
from .models import Person

#
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['nom', 'prenom', 'id', 'equipe']
