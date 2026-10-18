
from django.contrib import admin
from .models import Marca, Motocicleta


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "pais_origen")
    search_fields = ("nombre", "pais_origen")
    ordering = ("nombre",)


@admin.register(Motocicleta)
class MotocicletaAdmin(admin.ModelAdmin):
    list_display = (
        "modelo",
        "marca",
        "anio",
        "categoria",
        "cilindrada",
        "precio",
        "destacado",
        "disponible",
    )
    list_filter = ("marca", "categoria", "anio", "destacado", "disponible")
    search_fields = ("modelo", "marca__nombre")
    list_select_related = ("marca",)
    list_editable = ("destacado", "disponible")
    ordering = ("marca__nombre", "modelo")
    fieldsets = (
        ("Información general", {
            "fields": (
                "marca", "modelo", "anio", "categoria",
                "precio", "descripcion", "imagen_url",
                "destacado", "disponible",
            )
        }),
        ("Motor y rendimiento", {
            "fields": (
                "cilindrada", "potencia", "torque",
                "transmision", "refrigeracion", "alimentacion",
                "velocidad_maxima_kmh", "consumo_km_litro",
            )
        }),
        ("Dimensiones y componentes", {
            "fields": (
                "peso_kg", "altura_asiento_mm",
                "capacidad_tanque_litros",
                "freno_delantero", "freno_trasero",
                "suspension_delantera", "suspension_trasera",
            )
        }),
    )
