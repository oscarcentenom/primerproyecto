from django.urls import path
from ProyectoWebApp import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('resultados', views.resultados, name="Resultados"),
    path('descarga', views.descarga, name="Descarga"),
    path('quienes', views.quienes, name="Quienes"),
]