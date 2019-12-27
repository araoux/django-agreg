from django.shortcuts import render#,redirect, get_object_or_404
#from django.http import HttpResponse #, Http404

from .forms import RechercheInstrument
from .models import Instrument#, Notice

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
    form = RechercheInstrument(request.POST or None)
    if (form and form.is_valid()):
        show_results = True
        un_seul_instrument = False
        nom = form.cleaned_data['nom']
        ENSP = form.cleaned_data['ENSP']
        notice = form.cleaned_data['notice']
        liste_instruments = Instrument.objects.all().order_by('ENSP')
        
        if (nom):
            liste_instruments = Instrument.objects.filter(nom__contains=nom)
        if (ENSP):
            liste_instruments = Instrument.objects.filter(ENSP__contains=ENSP)
        if (notice):
            liste_instruments = Instrument.objects.filter(notice=notice)
        aumoinsunresultat = True ## A IMPLEMENTER
        
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'collection.html',locals())

def instrument(request, instr_ENSP):
    instr = Instrument.objects.filter(ENSP=instr_ENSP)[0]#.get(pk=1)
    aumoinsunresultat = True
    show_results = True
    un_seul_instrument = True
    
    return render(request, 'collection.html',locals())