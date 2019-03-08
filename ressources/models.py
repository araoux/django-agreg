from django.db import models

# Create your models here.

from django.utils import timezone


class Discipline(models.Model):
    nom = models.CharField(max_length=16)

    class Meta:
        verbose_name = "Discipline"
    def __str__(self):
        return self.nom

class Categorie(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom

class SousCategorie(models.Model):
    nom = models.CharField(max_length=30)
    cat_parent = models.ForeignKey(Categorie,on_delete=models.CASCADE,verbose_name="catégorie")

    class Meta:
        verbose_name = "Sous-catégorie"
    def __str__(self):
        return self.nom

class MotCle(models.Model):
    nom = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Mot-clé"
    def __str__(self):
        return self.nom

class Oral(models.Model):
    nom = models.CharField(max_length=100)
    numero = models.PositiveSmallIntegerField(verbose_name='n°')
    agreg = models.ForeignKey(Discipline, null=True, on_delete=models.SET_NULL)
    spe = models.BooleanField()
    ext = models.BooleanField(default=True)
    
    liste_oraux = (("LC","Leçon de chimie"),("LP","Leçon de physique"),("M","Montage"),("Dr","Mise en perspective didactique"))
    type_oral = models.CharField(max_length=2,choices=liste_oraux)

    class Meta:
        verbose_name = "Oraux"
    def __str__(self):
        afficher = str(self.agreg) + " " + self.type_oral + " " +  str(self.numero) + ". " + self.nom
        return afficher

class Ressource(models.Model):
    discipline = models.ForeignKey(Discipline,null=True,on_delete=models.SET_NULL)
    categorie = models.ForeignKey(Categorie,null=True,on_delete=models.SET_NULL,verbose_name="catégorie")
    sous_cat = models.ForeignKey(SousCategorie,null=True,on_delete=models.SET_NULL,verbose_name="sous-catégorie",blank=True)
    oral = models.ManyToManyField(Oral,blank=True)
    #auteur = models.CharField(max_length=42)
    description = models.TextField(null=True)
    mots_cles = models.ManyToManyField(MotCle,verbose_name="mots-clés",blank=True)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de parution")
    auteur = models.CharField(max_length=20)
    
    class Meta:
        verbose_name = "Ressource"
        ordering = ['date']

class RessourceImage(Ressource):
    contenu = models.ImageField()

class RessourceFichier(Ressource):
    contenu = models.FileField()

class RessourceScript(Ressource):
    contenu = models.FileField()

class RessourceLien(Ressource):
    contenu = models.URLField()

