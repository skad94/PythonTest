#Fichier définissant la vue pour modifier la BD via le formulaire
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.db.models import Q
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

##### Requete #####
## Recherche par personne

def rechercher_personnes(request):
    query = request.GET.get('query', '')
    if query:
        personnes = Person.objects.filter(Q(nom__icontains=query) | Q(prenom__icontains=query)) # type: ignore
    else:
        personnes = Person.objects.all()
    return render(request, 'rechercher_personnes.html', {'personnes': personnes, 'query': query}) # type: ignore


## Recherche par cle
def rechercher_personnes(request):
    query = request.GET.get('query', '')
    if query:
        personnes = Person.objects.filter(Q(nom__icontains=query) | Q(prenom__icontains=query)) # type: ignore
    else:
        personnes = Person.objects.all()
    return render(request, 'rechercher_personnes.html', {'personnes': personnes, 'query': query}) # type: ignore