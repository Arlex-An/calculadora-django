
from django.db import models


class Marca(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    pais_origen = models.CharField(max_length=100, blank=True)
    logo = models.URLField(blank=True)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "marca"
        verbose_name_plural = "marcas"

    def __str__(self):
        return self.nombre


class Motocicleta(models.Model):
    CATEGORIAS = [
        ("urbana", "Urbana"),
        ("deportiva", "Deportiva"),
        ("naked", "Naked"),
        ("adventure", "Adventure"),
        ("touring", "Touring"),
        ("scooter", "Scooter"),
        ("doble_proposito", "Doble propósito"),
        ("cruiser", "Cruiser"),
        ("otra", "Otra"),
    ]

    marca = models.ForeignKey(
        Marca,
        on_delete=models.PROTECT,
        related_name="motocicletas",
    )

    modelo = models.CharField(max_length=150)
    anio = models.PositiveSmallIntegerField("año")

    categoria = models.CharField(
        max_length=30,
        choices=CATEGORIAS,
        default="urbana",
    )

    precio = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
    )

    cilindrada = models.PositiveIntegerField(
        "cilindrada (cc)",
        null=True,
        blank=True,
    )

    potencia = models.CharField(max_length=60, blank=True)
    torque = models.CharField(max_length=60, blank=True)
    transmision = models.CharField(max_length=100, blank=True)
    refrigeracion = models.CharField(max_length=100, blank=True)
    alimentacion = models.CharField(max_length=100, blank=True)
    freno_delantero = models.CharField(max_length=150, blank=True)
    freno_trasero = models.CharField(max_length=150, blank=True)
    suspension_delantera = models.CharField(max_length=150, blank=True)
    suspension_trasera = models.CharField(max_length=150, blank=True)

    peso_kg = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
    )

    altura_asiento_mm = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
    )

    capacidad_tanque_litros = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
    )

    consumo_km_litro = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
    )

    velocidad_maxima_kmh = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
    )

    descripcion = models.TextField(blank=True)

    imagen_url = models.URLField(
        "URL de la fotografía principal",
        blank=True,
    )

    imagen_3d = models.URLField(
        "URL de la imagen 3D",
        blank=True,
    )

    sonido_motor = models.FileField(
        "sonido del motor",
        upload_to="sonidos_motos/",
        blank=True,
    )

    # Documento PDF de la ficha técnica de la motocicleta.
    ficha_pdf = models.FileField(
        "documento PDF de la ficha técnica",
        upload_to="fichas_tecnicas/",
        blank=True,
        null=True,
    )

    destacado = models.BooleanField(default=False)
    disponible = models.BooleanField(default=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["marca__nombre", "modelo", "-anio"]

        constraints = [
            models.UniqueConstraint(
                fields=["marca", "modelo", "anio"],
                name="motocicleta_marca_modelo_anio_unico",
            )
        ]

        verbose_name = "motocicleta"
        verbose_name_plural = "motocicletas"

    def __str__(self):
        return f"{self.marca.nombre} {self.modelo} ({self.anio})"
