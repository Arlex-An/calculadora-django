
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Marca, Motocicleta
from .forms import MarcaForm, MotocicletaForm


# ==========================================================
# CATÁLOGO PÚBLICO
# ==========================================================

def inicio(request):
    motos = Motocicleta.objects.filter(
        disponible=True
    ).select_related("marca")

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
        motos = motos.filter(
            cilindrada__gte=150,
            cilindrada__lt=250,
        )
    elif cilindrada == "250":
        motos = motos.filter(
            cilindrada__gte=250,
            cilindrada__lt=500,
        )
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


def detalle(request, moto_id):
    moto = get_object_or_404(
        Motocicleta.objects.select_related("marca"),
        pk=moto_id,
        disponible=True,
    )

    return render(
        request,
        "motos/detalle.html",
        {"moto": moto},
    )


def comparar(request):
    ids = request.GET.getlist("moto")

    motos = Motocicleta.objects.filter(
        pk__in=ids,
        disponible=True,
    ).select_related("marca")

    return render(
        request,
        "motos/comparar.html",
        {"motos": motos},
    )


# ==========================================================
# PANEL PRIVADO DE GESTIÓN
# Solo usuarios autenticados con permiso de personal
# ==========================================================


def gestionar(request):
    marcas = Marca.objects.all().order_by("nombre")

    motocicletas = Motocicleta.objects.select_related(
        "marca"
    ).all()

    return render(
        request,
        "motos/gestionar.html",
        {
            "marcas": marcas,
            "motocicletas": motocicletas,
        },
    )


# ==========================================================
# REGISTRAR MARCAS
# ==========================================================


def crear_marca(request):
    form = MarcaForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()

        messages.success(
            request,
            "La marca se registró correctamente.",
        )

        return redirect("gestionar_motos")

    return render(
        request,
        "motos/formulario_marca.html",
        {
            "form": form,
            "titulo": "Registrar marca",
        },
    )


# ==========================================================
# EDITAR MARCAS
# ==========================================================

def editar_marca(request, marca_id):
    marca = get_object_or_404(Marca, pk=marca_id)

    form = MarcaForm(
        request.POST or None,
        instance=marca,
    )

    if request.method == "POST" and form.is_valid():
        form.save()

        messages.success(
            request,
            "La marca se actualizó correctamente.",
        )

        return redirect("gestionar_motos")

    return render(
        request,
        "motos/formulario_marca.html",
        {
            "form": form,
            "titulo": "Editar marca",
        },
    )


# ==========================================================
# ELIMINAR MARCAS
# ==========================================================

def eliminar_marca(request, marca_id):
    marca = get_object_or_404(Marca, pk=marca_id)

    if request.method == "POST":
        try:
            marca.delete()

            messages.success(
                request,
                "La marca se eliminó correctamente.",
            )

        except Exception:
            messages.error(
                request,
                "No se puede eliminar esta marca porque "
                "tiene motocicletas asociadas.",
            )

        return redirect("gestionar_motos")

    return render(
        request,
        "motos/confirmar_eliminacion.html",
        {
            "objeto": marca,
            "tipo": "marca",
        },
    )


# ==========================================================
# REGISTRAR MOTOCICLETAS
# ==========================================================


def crear_motocicleta(request):
    form = MotocicletaForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()

        messages.success(
            request,
            "La motocicleta se registró correctamente.",
        )

        return redirect("gestionar_motos")

    return render(
        request,
        "motos/formulario_moto.html",
        {
            "form": form,
            "titulo": "Registrar motocicleta",
        },
    )


# ==========================================================
# EDITAR MOTOCICLETAS
# ==========================================================

def editar_motocicleta(request, moto_id):
    moto = get_object_or_404(
        Motocicleta,
        pk=moto_id,
    )

    form = MotocicletaForm(
        request.POST or None,
        instance=moto,
    )

    if request.method == "POST" and form.is_valid():
        form.save()

        messages.success(
            request,
            "La motocicleta se actualizó correctamente.",
        )

        return redirect("gestionar_motos")

    return render(
        request,
        "motos/formulario_moto.html",
        {
            "form": form,
            "titulo": "Editar motocicleta",
        },
    )


# ==========================================================
# ELIMINAR MOTOCICLETAS
# ==========================================================


def eliminar_motocicleta(request, moto_id):
    moto = get_object_or_404(
        Motocicleta,
        pk=moto_id,
    )

    if request.method == "POST":
        moto.delete()

        messages.success(
            request,
            "La motocicleta se eliminó correctamente.",
        )

        return redirect("gestionar_motos")

    return render(
        request,
        "motos/confirmar_eliminacion.html",
        {
            "objeto": moto,
            "tipo": "motocicleta",
        },
    )
