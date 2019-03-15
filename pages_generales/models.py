from django.db import models

from django.utils import timezone
# Create your models here.

class Notice(models.Model):
    numero = models.SmallIntegerField()
    commentaire = models.CharField(max_length=64, blank=True,null=True)
    fichier = models.FileField(null=True)

    class Meta:
        verbose_name = "Statut"
    def __str__(self):
        afficher = str(self.nom)
        return afficher

class Statut(models.Model):
    nom = models.CharField(max_length=64)

    class Meta:
        verbose_name = "Statut"
    def __str__(self):
        afficher = str(self.nom)
        return afficher

class Rangee(models.Model):
    nom = models.CharField(max_length=64)

    class Meta:
        verbose_name = "Rangée"
    def __str__(self):
        afficher = str(self.nom)
        return afficher

class Colonne(models.Model):
    nom = models.CharField(max_length=64)

    class Meta:
        verbose_name = "Colonne"
    def __str__(self):
        afficher = str(self.nom)
        return afficher

class Etagere(models.Model):
    nom = models.CharField(max_length=64)

    class Meta:
        verbose_name = "Étagère"
    def __str__(self):
        afficher = str(self.nom)
        return afficher

class Categorie(models.Model):
    nom = models.CharField(max_length=64)

    class Meta:
        verbose_name = "Catégorie"
    def __str__(self):
        afficher = str(self.nom)
        return afficher


class Theme(models.Model):
    nom = models.CharField(max_length=64)

    class Meta:
        verbose_name = "Thème"
    def __str__(self):
        afficher = str(self.nom)
        return afficher

class Instrument(models.Model):
    nom = models.CharField(max_length=64)
    ENSP = models.SmallIntegerField()
    notice = models.ForeignKey(Notice, on_delete='SET_NULL', null=True, blank=True)
    ref = models.CharField(max_length=64, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(blank=True,null=True)
    statut = models.ForeignKey(Statut, on_delete='SET_NULL', null=True)
    categorie = models.ForeignKey(Categorie, on_delete='SET_NULL', null=True)
    theme = models.ForeignKey(Theme, on_delete='SET_NULL', null=True)
    rangee = models.ForeignKey(Rangee, on_delete='SET_NULL', null=True)
    colonne = models.ForeignKey(Colonne, on_delete='SET_NULL', null=True)
    etagere = models.ForeignKey(Etagere, on_delete='SET_NULL', null=True)
    date_ajout = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = "Instrument"
    def __str__(self):
        afficher = str(self.nom)
        return afficher