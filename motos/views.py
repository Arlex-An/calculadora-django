
from django.db.models import Q
from django.shortcuts import render
from .models import Marca, Motocicleta


def inicio(request):
    motos = Motocicleta.objects.filter(disponible=True).select_related("marca")
    marcas = Marca.objects.all()

    busqueda = request.GET.get("q", "").strip()
    marca_id = request.GET.get("marca", "")
    categoria = request.GET.get("categoria", "")
    cilindrada = request.GET.get("cilindrada", "")

    if busqueda:
        motos = motos.filter(
            Q(modelo__icontains=busqueda)
            | Q(marca__nombre__icontains=busqueda)
            | Q(descripcion__icontains=busqueda)
        )

    if marca_id.isdigit():
        motos = motos.filter(marca_id=int(marca_id))

    if categoria:
        motos = motos.filter(categoria=categoria)

    if cilindrada == "125":
        motos = motos.filter(cilindrada__lt=150)
    elif cilindrada == "150":
        motos = motos.filter(cilindrada__gte=150, cilindrada__lt=250)
    elif cilindrada == "250":
        motos = motos.filter(cilindrada__gte=250, cilindrada__lt=500)
    elif cilindrada == "500":
        motos = motos.filter(cilindrada__gte=500)

    return render(
        request,
        "motos/inicio.html",
        {
            "motos": motos,
            "marcas": marcas,
            "categorias": Motocicleta.CATEGORIAS,
            "busqueda": busqueda,
            "marca_seleccionada": marca_id,
            "categoria_seleccionada": categoria,
            "cilindrada_seleccionada": cilindrada,
        },
    )




from django.shortcuts import render, get_object_or_404
from .models import Motocicleta


def detalle(request, moto_id):
    moto = get_object_or_404(
        Motocicleta.objects.select_related("marca"),
        pk=moto_id,
        disponible=True,
    )
    return render(request, "motos/detalle.html", {"moto": moto})




def comparar(request):
    ids = request.GET.getlist("moto")
    motos = Motocicleta.objects.filter(
        pk__in=ids,
        disponible=True,
    ).select_related("marca")

    return render(request, "motos/comparar.html", {"motos": motos})
