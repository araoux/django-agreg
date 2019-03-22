from django.contrib import admin

# Register your models here.
from .models import *

class InstrumentAdmin(admin.ModelAdmin):
   list_display   = ('ENSP', 'nom','notice','rangee','colonne','etagere','statut','categorie')
   list_filter    = ('categorie','rangee','statut')
   ordering       = ('nom','ENSP','id', )
   search_fields  = ('nom', 'notice','ENSP')
   
   # Modification de la page d'édition
   fields = ('nom','ENSP','notice','ref', 'description','image','statut','categorie','theme','rangee','colonne','etagere')




admin.site.register(Instrument,InstrumentAdmin)
#admin.site.register(Categorie)
#admin.site.register(Theme)
#admin.site.register(Etagere)
#admin.site.register(Colonne)
#admin.site.register(Rangee)
admin.site.register(Notice)
#admin.site.register(Statut)
