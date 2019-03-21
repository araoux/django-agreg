from django.shortcuts import render#,redirect, get_object_or_404
#from django.http import HttpResponse, Http404

from .forms import RechercheInstrument
from .models import Instrument

import config

# Create your views here.

def candidater(request):
    lien_SU_master = config.lien_SU_master
    lien_P11_magistere = config.lien_P11_magistere
    return render(request, 'candidater.html',locals())

def formation(request):
    site_agreg_ext = config.site_agreg_ext
    site_agreg_spe = config.site_agreg_spe
    programme_officiel_ext = config.programme_officiel_ext
    programme_officiel_spe = config.programme_officiel_spe
    lien_resultats_centre = config.lien_resultats_centre
    return render(request, 'formation.html',locals())

def index(request):
    return render(request, 'index.html',locals())

def infos(request):
    lien_SU_master = config.lien_SU_master
    lien_P11_magistere = config.lien_P11_magistere
    return render(request, 'infos.html',locals())

def collection(request):
    
#    if (request.GET['id']):
#        show_results = True
#        unique_resultat = True
#        id_instr = int(request.GET['id'])
#        instrument = Instrument.objects.filter(id=id_instr)
#        return render(request, 'collection.html?id='.str(id_instr),locals())
#    
#    else:
        form = RechercheInstrument(request.POST or None)
        if form.is_valid():
            show_results = True
            nom = form.cleaned_data['nom']
            ENSP = form.cleaned_data['ENSP']
            notice = form.cleaned_data['notice']
            liste_instruments = Instrument.objects.all()
            
            aumoinsunresultat = True ## A IMPLEMENTER
            
        # Quoiqu'il arrive, on affiche la page du formulaire.
        return render(request, 'collection.html',locals())