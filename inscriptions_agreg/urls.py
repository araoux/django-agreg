from django.urls import path
from . import views

urlpatterns = [
    path('accueil/', views.accueil, name="accueil"),
    path('connection/', views.connection, name="connection"),
]
