from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Ressource, RessourceLien, RessourceScript, RessourceImage, RessourceFichier, Discipline,Oral
# Create your views here.

from .forms import RessourceForm, RessourceParOralForm

def recherche(request):
    # Construire le formulaire, soit avec les données postées, soit vide si l'utilisateur accède pour la première fois à la page.
    form = RessourceForm(request.POST or None)
    form2 = RessourceParOralForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides. Cette méthode renvoie False s'il n'y a pas de données dans le formulaire ou qu'il contient des erreurs.
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
        
        aumoinsunresultat = True

    elif form2.is_valid(): 
        show_result = True
        agreg = form2.cleaned_data['agreg']
        type_oral = form2.cleaned_data['type_oral']
        numero = form2.cleaned_data['numero']

        aumoinsunresultat = list(Oral.objects.filter(agreg=agreg,type_oral=type_oral,numero=numero))
        
        if aumoinsunresultat:
            oral = aumoinsunresultat[0]
            liste_liens = RessourceLien.objects.filter(oral__agreg=agreg,oral__type_oral=type_oral,oral__numero=numero)
            liste_images = RessourceImage.objects.filter(oral__agreg=agreg,oral__type_oral=type_oral,oral__numero=numero)
            liste_scripts = RessourceScript.objects.filter(oral__agreg=agreg,oral__type_oral=type_oral,oral__numero=numero)
            liste_fichiers = RessourceFichier.objects.filter(oral__agreg=agreg,oral__type_oral=type_oral,oral__numero=numero)

    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'ressources/recherche.html', locals())