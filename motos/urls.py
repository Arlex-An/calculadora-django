
from django.urls import path
from . import views

urlpatterns = [
    # Páginas del catálogo
    path("", views.inicio, name="inicio"),
    path("moto/<int:moto_id>/", views.detalle, name="detalle_moto"),
    path("comparar/", views.comparar, name="comparar_motos"),

    # Página para gestionar motocicletas y marcas
    path("gestionar-motos/", views.gestionar, name="gestionar_motos"),

    # Registrar, editar y eliminar marcas
    path(
        "gestionar-motos/marcas/nueva/",
        views.crear_marca,
        name="crear_marca",
    ),
    path(
        "gestionar-motos/marcas/<int:marca_id>/editar/",
        views.editar_marca,
        name="editar_marca",
    ),
    path(
        "gestionar-motos/marcas/<int:marca_id>/eliminar/",
        views.eliminar_marca,
        name="eliminar_marca",
    ),

    # Registrar, editar y eliminar motocicletas
    path(
        "gestionar-motos/motos/nueva/",
        views.crear_motocicleta,
        name="crear_motocicleta",
    ),
    path(
        "gestionar-motos/motos/<int:moto_id>/editar/",
        views.editar_motocicleta,
        name="editar_motocicleta",
    ),
    path(
        "gestionar-motos/motos/<int:moto_id>/eliminar/",
        views.eliminar_motocicleta,
        name="eliminar_motocicleta",
    ),
]
