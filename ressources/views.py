from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Ressource, RessourceLien, RessourceScript, RessourceImage, RessourceFichier, Discipline
# Create your views here.

def accueil(request):
    return render(request, 'ressources/accueil.html')

from .forms import RessourceForm

def recherche(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = RessourceForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.
    
    if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
        show_result = True
        formulaire = form.cleaned_data
        
        filtres = {}
        for key, value in formulaire.items():
            if (value):
                filtres[key]=value
        
        filtres_definis=filtres.keys()
        
        liste_liens = RessourceLien.objects.all()
        liste_images = RessourceImage.objects.all()
        liste_scripts = RessourceScript.objects.all()
        liste_fichiers = RessourceFichier.objects.all()

        
        if 'discipline' in filtres_definis:
            liste_liens = RessourceLien.objects.filter(discipline__nom=filtres['discipline'])
            liste_images = RessourceImage.objects.filter(discipline__nom=filtres['discipline'])
            liste_scripts = RessourceScript.objects.filter(discipline__nom=filtres['discipline'])
            liste_fichiers = RessourceFichier.objects.filter(discipline__nom__contains=filtres['discipline'])
        
        if 'categorie' in filtres_definis:
            liste_liens = liste_liens.filter(categorie__nom=filtres['categorie'])
            liste_images = liste_images.filter(categorie__nom=filtres['categorie'])
            liste_scripts = liste_scripts.filter(categorie__nom=filtres['categorie'])
            liste_fichiers = liste_fichiers.filter(categorie__nom=filtres['categorie'])

        if 'sous_cat' in filtres_definis:
            liste_liens = liste_liens.filter(sous_cat__nom=filtres['sous_cat'])
            liste_images = liste_images.filter(sous_cat__nom=filtres['sous_cat'])
            liste_scripts = liste_scripts.filter(sous_cat__nom=filtres['sous_cat'])
            liste_fichiers = liste_fichiers.filter(sous_cat__nom=filtres['sous_cat'])
        
        if 'mot_cle' in filtres_definis:
            liste_liens = liste_liens.filter(mot_cle__first=filtres['mot_cle'])


    test = Discipline.objects.get(pk=2)
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'ressources/accueil.html', locals())