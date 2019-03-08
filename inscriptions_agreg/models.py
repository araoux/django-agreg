from django.db import models

from django.utils import timezone
# Create your models here.

class Centre(models.Model):
    nom = models.CharField(max_length=30,verbose_name="nom")

    class Meta:
        verbose_name = "Centres"
    def __str__(self):
        afficher = str(self.nom)
        return afficher

class Candidat(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    date_naissance = models.DateField()
    telephone = models.CharField(max_length=100)
    nationalite = models.CharField(max_length=20)
    date_inscription = models.DateField()

    class Meta:
        verbose_name = "Candidats"
    def __str__(self):
        afficher = str(self.nom)
        return afficher

class Inscription(models.Model):

    auteur = models.ForeignKey(Candidat, on_delete=models.SET_NULL,null=True)
    situation_actuelle = models.CharField(max_length=100)
    situation_prochaine = models.CharField(max_length=100)
    situation_post_agreg = models.CharField(max_length=100)
    cv = models.FileField()
    deja_candidat = models.BooleanField()
    deja_candidat_annee = models.DateField()
    autres_centres = models.ManyToManyField(Centre)
    
    # CONCOURS ENSEIGNEMENT
    capes = models.BooleanField()
    capes_annee = models.DateField()
    agregation = models.BooleanField()
    agregation_annee = models.DateField()
    agregation_resultats = models.FileField()
    
    # PARCOURS
    annees_scolaires= []
    for year in range(1990, (timezone.now().year+1)):
        annee = str(year)+'-'+str(year+1)
        annees_scolaires.append((annee,annee))
    
    bac =  models.DateField()
    L1_annee = models.CharField(choices = annees_scolaires,max_length=15)
    L1_etablissement = models.CharField(max_length=100)
    L1_filiere = models.CharField(max_length=100)
    
    L2_annee = models.CharField(choices = annees_scolaires,max_length=15)
    L2_etablissement = models.CharField(max_length=100)
    L2_filiere = models.CharField(max_length=100)

    L3_annee = models.CharField(choices = annees_scolaires,max_length=15)
    L3_etablissement = models.CharField(max_length=100)
    L3_filiere = models.CharField(max_length=100)

    M1_annee = models.CharField(choices = annees_scolaires,max_length=15)
    M1_etablissement = models.CharField(max_length=100)
    M1_filiere = models.CharField(max_length=100)

    M2_annee = models.CharField(choices = annees_scolaires,max_length=15)
    M2_etablissement = models.CharField(max_length=100)
    M2_filiere = models.CharField(max_length=100)
    
    resultats = models.FileField(default=None)
    
    doctorat = models.BooleanField(default=False)
    doctorat_date = models.DateField()
    doctorat_titre = models.CharField(max_length=100)
    doctorat_directeur = models.CharField(max_length=100)
    
    voie = models.CharField(choices = (('ext','Voie standard'),('spe','Voie Docteurs')),max_length=15)
    
    recomandation = models.FileField()
    commentaires = models.TextField()
    date_inscription = models.DateField()
    
    class Meta:
        verbose_name = "Inscriptions"
#    def __str__(self):
#        afficher = str(self.agreg) + " " + self.type_oral + " " +  str(self.numero) + ". " + self.nom
#        return afficher