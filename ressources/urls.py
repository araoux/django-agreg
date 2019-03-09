from django.urls import path
from . import views

urlpatterns = [
    path('recherche/', views.recherche, name="recherche"),
#    path('recherche/', views.recherche_par_oral, name="recherche_par_oral"),
]
