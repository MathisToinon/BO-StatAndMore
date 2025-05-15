from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('comparaison/', views.comparaison, name='comparaison'),
    path('secteur/', views.secteur, name='secteur'),
    path('carte/', views.carte, name='carte'),
]