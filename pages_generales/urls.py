from django.urls import path
from . import views

urlpatterns = [
    path("candidater", views.candidater, name="candidater"),
    path("formation", views.formation, name="formation"),
    path("index", views.index, name="index"),
    path("infos", views.infos, name="infos"),
    path("", views.index),
    path("collection", views.collection, name="collection"),
    ]
