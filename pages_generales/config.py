import os
from django.conf import settings

def renommage_notice(instance, nom_fichier):
    return "collection/{}s/N_{}.pdf".format(instance.__class__.__name__,instance.numero)

def renommage_image(instance, nom_fichier):
    ext = os.path.splitext(nom_fichier)[-1]
    return "collection/{}s/ENSP_{}{}".format(instance.__class__.__name__,instance.ENSP,ext)