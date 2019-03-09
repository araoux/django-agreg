from django import forms
# Create your forms here.

#from django.utils import timezone
from .models import Ressource, Oral

class RessourceForm(forms.ModelForm):
    
    class Meta:
        model = Ressource
#        
#        widgets = {
#            'mots_cles': forms.Textarea(attrs={'cols': 15, 'rows': 1}),
#           # 'oral':forms.Select(),
#        }
        fields = ['discipline','categorie', 'sous_cat']#, 'oral', 'mots_cles']
    def __init__(self, *args, **kwargs):
        super(RessourceForm, self).__init__(*args, **kwargs)
        self.fields['discipline'].required = True
        self.fields['categorie'].required = True
        self.fields['sous_cat'].required = False
        #self.fields['oral'].required = False
        #self.fields['mots_cles'].required = False


class RessourceParOralForm(forms.ModelForm):
    
    class Meta:
        model = Oral
        
        fields = ['agreg','type_oral','numero',]
        
    def __init__(self, *args, **kwargs):
        super(RessourceParOralForm, self).__init__(*args, **kwargs)
        self.fields['agreg'].required = True
        self.fields['type_oral'].required = True
        self.fields['numero'].required = True