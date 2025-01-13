from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Laboratorio
from .forms import LaboratorioForm


def laboratorio_list(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, "laboratorio_list.html", {"laboratorios": laboratorios})


def laboratorio_detail(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    return render(request, "laboratorio_detail.html", {"laboratorio": laboratorio})


def laboratorio_new(request):
    if request.method == "POST":
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            laboratorio = form.save()
            return redirect("laboratorio_detail", pk=laboratorio.pk)
    else:
        form = LaboratorioForm()
    return render(request, "laboratorio_new.html", {"form": form})


def laboratorio_edit(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == "POST":
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            laboratorio = form.save()
            return redirect("laboratorio_detail", pk=laboratorio.pk)
    else:
        form = LaboratorioForm(instance=laboratorio)
    return render(request, "laboratorio_edit.html", {"form": form})


def laboratorio_delete(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == "POST":
        laboratorio.delete()
        return redirect("laboratorio_list")
    return render(
        request,
        "laboratorio_confirm_delete.html",
        {"laboratorio": laboratorio},
    )
