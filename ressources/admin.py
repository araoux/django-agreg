from django.contrib import admin

# Register your models here.
from .models import Ressource,Categorie,SousCategorie,Discipline,Oral,MotCle,RessourceImage,RessourceFichier,RessourceLien,RessourceScript

class RessourceAdmin(admin.ModelAdmin):
   list_display   = ('description', 'categorie','sous_cat')
   list_filter    = ('categorie','sous_cat','oral','mots_cles',)
   date_hierarchy = 'date'
   ordering       = ('date', )
   search_fields  = ('description', 'mots_cles')
   
   # Modification de la page d'édition
   fields = ('contenu','description', 'discipline','categorie','sous_cat','oral','mots_cles')

class SousCategorieAdmin(admin.ModelAdmin):
   list_display   = ('nom', 'cat_parent')
   list_filter    = ('cat_parent',)
   ordering       = ('cat_parent', )
   search_fields  = ('nom',)

class OralAdmin(admin.ModelAdmin):
   list_display   = ('agreg', 'numero','type_oral','spe','nom')
   list_filter    = ('agreg','type_oral','spe',)
   ordering       = ('agreg','type_oral','numero', )
   search_fields  = ('nom', 'numero')
   
   # Modification de la page d'édition
   fields = ('agreg','type_oral','numero','nom', 'ext','spe')

class CategorielAdmin(admin.ModelAdmin):
   list_display   = ('nom', 'discipline')
   list_filter    = ( 'discipline',)
   ordering       = ( 'discipline', 'nom')
   search_fields  = ('nom',)
   
   # Modification de la page d'édition
   fields = ('nom', 'discipline')


#admin.site.register(Discipline)
admin.site.register(Categorie)
admin.site.register(SousCategorie, SousCategorieAdmin)
admin.site.register(Oral,OralAdmin)
admin.site.register(MotCle)

admin.site.register(RessourceImage,RessourceAdmin)
admin.site.register(RessourceFichier,RessourceAdmin)
admin.site.register(RessourceScript,RessourceAdmin)
admin.site.register(RessourceLien,RessourceAdmin)
