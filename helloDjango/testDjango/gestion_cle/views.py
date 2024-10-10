#Fichier définissant la vue pour modifier la BD via le formulaire
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
# Pour info: pour enlever le warning on a ajouté le #type: ignore de la ligne en dessous
from .forms import PersonForm #type: ignore

def ajouter_personne(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ajouter_personne')
    else:
        form = PersonForm()
    return render(request, 'ajouter_personne.html', {'form': form})

def home(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ajouter_personne')
    else:
        form = PersonForm()
    return render(request, 'home.html', {'form': form})  # Assure-toi d'avoir un template 'home.html'