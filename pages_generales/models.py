from django.db import models

from django.utils import timezone
# Create your models here.

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
    notice = models.SmallIntegerField()
    ref = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField()
    statut = models.CharField(max_length=20)
    lien = models.URLField()
    categorie = models.ForeignKey(Categorie, on_delete='CASCADE')
    theme = models.ForeignKey(Theme, on_delete='CASCADE')
    rangee = models.SmallIntegerField()
    colonne = models.SmallIntegerField()
    etagere = models.SmallIntegerField()
    date_ajout = models.DateField()

    class Meta:
        verbose_name = "Instrument"
    def __str__(self):
        afficher = str(self.nom)
        return afficher