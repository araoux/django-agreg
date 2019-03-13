from django.urls import path
from . import views

urlpatterns = [
    path('', views.recherche_accueil, name="recherche_accueil"),
    path('recherche_categorie/', views.recherche_categorie, name="recherche_categorie"),
    path('recherche_oral/', views.recherche_oral, name="recherche_oral"),
    path('recherche_tous/', views.recherche_tous, name="recherche_tous"),
]
