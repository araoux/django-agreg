from django import forms
# Create your forms here.

from django.utils import timezone
from .models import Inscription

class InscriptionForm(forms.ModelForm):
    
    class Meta:
        model = Inscription
    
        exclude=[]

