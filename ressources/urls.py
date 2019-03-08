from django.urls import path
from . import views

urlpatterns = [
    path('accueil/', views.accueil, name="accueil"),
    path('recherche/', views.recherche, name='recherche'),
]
