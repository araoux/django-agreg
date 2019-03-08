from django import forms
# Create your forms here.

from django.utils import timezone
from .models import Ressource, Discipline

class RessourceForm(forms.ModelForm):
    
    class Meta:
        model = Ressource
        
        widgets = {
            'mots_cles': forms.Textarea(attrs={'cols': 15, 'rows': 1}),
           # 'oral':forms.Select(),
        }
        fields = ['discipline','categorie', 'sous_cat', 'oral', 'mots_cles']
    def __init__(self, *args, **kwargs):
        super(RessourceForm, self).__init__(*args, **kwargs)
        self.fields['discipline'].required = False
        self.fields['categorie'].required = False
        self.fields['sous_cat'].required = False
        self.fields['oral'].required = False
        self.fields['mots_cles'].required = False

