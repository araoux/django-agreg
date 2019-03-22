from django import forms
# Create your forms here.

#from django.utils import timezone
from .models import Instrument

class RechercheInstrument(forms.ModelForm):
    
    class Meta:
        model = Instrument
#        
#        widgets = {
#            'mots_cles': forms.Textarea(attrs={'cols': 15, 'rows': 1}),
#           # 'oral':forms.Select(),
#        }
        fields = ['nom','ENSP', 'notice']#, 'oral', 'mots_cles']
    def __init__(self, *args, **kwargs):
        super(RechercheInstrument, self).__init__(*args, **kwargs)
        self.fields['nom'].required = False
        self.fields['ENSP'].required = False
        self.fields['notice'].required = False