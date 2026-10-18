
from django import forms
from .models import Marca, Motocicleta


class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = [
            "nombre",
            "pais_origen",
            "logo",
        ]

        widgets = {
            "nombre": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ej. Yamaha",
            }),
            "pais_origen": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ej. Japón",
            }),
            "logo": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "https://ejemplo.com/logo.png",
            }),
        }


class MotocicletaForm(forms.ModelForm):
    class Meta:
        model = Motocicleta

        fields = [
            "marca",
            "modelo",
            "anio",
            "categoria",
            "precio",
            "cilindrada",
            "potencia",
            "torque",
            "transmision",
            "refrigeracion",
            "alimentacion",
            "freno_delantero",
            "freno_trasero",
            "suspension_delantera",
            "suspension_trasera",
            "peso_kg",
            "altura_asiento_mm",
            "capacidad_tanque_litros",
            "consumo_km_litro",
            "velocidad_maxima_kmh",
            "descripcion",
            "imagen_url",
            "destacado",
            "disponible",
        ]

        widgets = {
            "descripcion": forms.Textarea(attrs={
                "rows": 4,
            }),
            "imagen_url": forms.URLInput(attrs={
                "placeholder": "https://ejemplo.com/moto.jpg",
            }),
            "precio": forms.NumberInput(attrs={
                "min": "0",
                "step": "0.01",
            }),
            "anio": forms.NumberInput(attrs={
                "min": "1900",
                "max": "2100",
            }),
        }
