from django.shortcuts import render

# Create your views here.

from .forms import InscriptionForm

def accueil(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = InscriptionForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.
    
    if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
        show_result = True
        formulaire = form.cleaned_data
        
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'ressources/accueil.html', locals())


def connection(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ConnectionForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.
    
    if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
        show_result = True
        formulaire = form.cleaned_data
        
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'ressources/accueil.html', locals())