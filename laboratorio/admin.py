from django.contrib import (
    admin,
)  # Importa las herramientas para registrar modelos en el panel de administración de Django

# Importa los modelos que se registrarán en el panel administrativo
from .models import Laboratorio, DirectorGeneral, Producto


# Registra el modelo Laboratorio en el panel administrativo
@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    # Define qué campos del modelo Laboratorio se mostrarán en la lista administrativa
    list_display = ("nombre",)  # Muestra solo el campo 'nombre' en la lista


# Registra el modelo DirectorGeneral en el panel administrativo
@admin.register(DirectorGeneral)
class DirectorGeneralAdmin(admin.ModelAdmin):
    # Define qué campos del modelo DirectorGeneral se mostrarán en la lista administrativa
    list_display = (
        "nombre",
        "laboratorio",
    )  # Muestra los campos 'nombre' y el laboratorio asociado


# Registra el modelo Producto en el panel administrativo
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # Define qué campos del modelo Producto se mostrarán en la lista administrativa
    list_display = ("nombre", "laboratorio", "f_fabricacion", "p_costo", "p_venta")
    # Agrega filtros laterales para los campos 'laboratorio' y 'nombre'
    list_filter = ("laboratorio", "nombre")
    # Permite buscar productos por su nombre o por el nombre del laboratorio relacionado
    search_fields = ("nombre", "laboratorio__nombre")
