from django.contrib import admin

# Register your models here.

from .models import Centre,Inscription,Candidat

class InscriptionAdmin(admin.ModelAdmin):
   list_display   = ('auteur','bac',)
   list_filter    = ('auteur','bac',)
   date_hierarchy = 'date_inscription'
   ordering       = ('date_inscription', )
   #search_fields  = ('nom',)
   
   # Modification de la page d'édition
   #fields = ('contenu','description', 'discipline','categorie','sous_cat','oral','mots_cles')

class CentreAdmin(admin.ModelAdmin):
   list_display   = ('nom',)

class CandidatAdmin(admin.ModelAdmin):
   list_display   = ('nom','prenom','email')
   list_filter    = ('nom', 'prenom','email',)
   date_hierarchy = 'date_inscription'
   ordering       = ('date_inscription', )
   search_fields  = ('nom',)

admin.site.register(Inscription)
admin.site.register(Centre,CentreAdmin)
admin.site.register(Candidat,CandidatAdmin)