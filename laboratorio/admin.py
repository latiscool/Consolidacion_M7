from django.contrib import admin

# Register your models here.
from .models import Laboratorio, DirectorGeneral, Producto


@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ("nombre",)


@admin.register(DirectorGeneral)
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ("nombre", "laboratorio")


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "laboratorio", "f_fabricacion", "p_costo", "p_venta")
    list_filter = ("laboratorio", "nombre")
    search_fields = ("nombre", "laboratorio__nombre")
