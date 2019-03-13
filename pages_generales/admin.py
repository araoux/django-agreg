from django.contrib import admin

# Register your models here.
from .models import Instrument,Categorie,Theme

class InstrumentAdmin(admin.ModelAdmin):
   list_display   = ('id', 'nom','ENSP','notice','nom')
   list_filter    = ('categorie',)
   ordering       = ('nom','ENSP','id', )
   search_fields  = ('nom', 'notice','ENSP')
   
   # Modification de la page d'édition
   #fields = ('agreg','type_oral','numero','nom', 'ext','spe')




admin.site.register(Instrument,InstrumentAdmin)
admin.site.register(Categorie)
admin.site.register(Theme)
