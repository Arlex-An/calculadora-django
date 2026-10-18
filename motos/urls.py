
from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("moto/<int:moto_id>/", views.detalle, name="detalle_moto"),
    path("comparar/", views.comparar, name="comparar_motos"),
]
