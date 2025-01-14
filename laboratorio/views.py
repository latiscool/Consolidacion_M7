from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Laboratorio
from .forms import LaboratorioForm


# Vista para listar todos los laboratorios
def laboratorio_list(request):
    # Obtiene todos los objetos del modelo Laboratorio
    laboratorios = Laboratorio.objects.all()
    # Renderiza la plantilla "laboratorio_list.html" y pasa los laboratorios como contexto
    return render(request, "laboratorio_list.html", {"laboratorios": laboratorios})


# Vista para mostrar los detalles de un laboratorio específico
def laboratorio_detail(request, pk):
    # Busca un laboratorio por su clave primaria (pk) o lanza un error 404 si no se encuentra
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    # Renderiza la plantilla "laboratorio_detail.html" y pasa el laboratorio como contexto
    return render(request, "laboratorio_detail.html", {"laboratorio": laboratorio})


# Vista para crear un nuevo laboratorio
def laboratorio_new(request):
    # Si el método de la solicitud es POST (formulario enviado)
    if request.method == "POST":
        # Crea un formulario con los datos enviados
        form = LaboratorioForm(request.POST)
        # Verifica si los datos del formulario son válidos
        if form.is_valid():
            # Guarda el nuevo laboratorio en la base de datos
            laboratorio = form.save()
            # Redirige a la vista de detalles del nuevo laboratorio creado
            return redirect("laboratorio_detail", pk=laboratorio.pk)
    else:
        # Si la solicitud es GET (mostrar el formulario vacío)
        form = LaboratorioForm()
    # Renderiza la plantilla "laboratorio_new.html" y pasa el formulario como contexto
    return render(request, "laboratorio_new.html", {"form": form})


# Vista para editar un laboratorio existente
def laboratorio_edit(request, pk):
    # Busca un laboratorio por su clave primaria (pk) o lanza un error 404 si no se encuentra
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    # Si el método de la solicitud es POST (formulario enviado)
    if request.method == "POST":
        # Crea un formulario con los datos enviados y asocia el laboratorio existente
        form = LaboratorioForm(request.POST, instance=laboratorio)
        # Verifica si los datos del formulario son válidos
        if form.is_valid():
            # Guarda los cambios en el laboratorio existente en la base de datos
            laboratorio = form.save()
            # Redirige a la vista de detalles del laboratorio editado
            return redirect("laboratorio_detail", pk=laboratorio.pk)
    else:
        # Si la solicitud es GET (mostrar el formulario con los datos actuales del laboratorio)
        form = LaboratorioForm(instance=laboratorio)
    # Renderiza la plantilla "laboratorio_edit.html" y pasa el formulario como contexto
    return render(request, "laboratorio_edit.html", {"form": form})


# Vista para eliminar un laboratorio existente
def laboratorio_delete(request, pk):
    # Busca un laboratorio por su clave primaria (pk) o lanza un error 404 si no se encuentra
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    # Si el método de la solicitud es POST (confirmación de eliminación enviada)
    if request.method == "POST":
        # Elimina el laboratorio de la base de datos
        laboratorio.delete()
        # Redirige a la vista que lista todos los laboratorios
        return redirect("laboratorio_list")
    # Renderiza la plantilla "laboratorio_confirm_delete.html" y pasa el laboratorio como contexto
    return render(
        request,
        "laboratorio_confirm_delete.html",
        {"laboratorio": laboratorio},
    )
