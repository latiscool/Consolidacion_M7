from django.db import models  # Importa las herramientas para definir modelos en Django
from django.core.validators import (
    MinValueValidator,
)  # Importa un validador para restringir valores mínimos
from django.utils import timezone  # Importa utilidades relacionadas con fechas y horas

# Define los modelos de la aplicación aquí


# Modelo que representa un laboratorio
class Laboratorio(models.Model):
    # Campo de texto para el nombre del laboratorio (máximo 100 caracteres)
    nombre = models.CharField(max_length=100)
    # Campo de texto para la ciudad donde se encuentra el laboratorio (máximo 100 caracteres)
    ciudad = models.CharField(max_length=100)
    # Campo de texto para el país donde se encuentra el laboratorio (máximo 100 caracteres)
    pais = models.CharField(max_length=100)

    # Método especial para representar el objeto como una cadena (nombre del laboratorio)
    def __str__(self):
        return self.nombre


# Modelo que representa al director general de un laboratorio
class DirectorGeneral(models.Model):
    # Campo de texto para el nombre del director general (máximo 100 caracteres)
    nombre = models.CharField(max_length=100)
    # Relación uno a uno con el modelo Laboratorio
    # Si se elimina el laboratorio, también se elimina al director asociado (on_delete=models.CASCADE)
    laboratorio = models.OneToOneField(
        Laboratorio, on_delete=models.CASCADE, related_name="director"
    )
    # Campo de texto para la especialidad del director general (máximo 100 caracteres)
    especialidad = models.CharField(max_length=100)

    # Clase interna Meta para personalizar nombres en la interfaz administrativa de Django
    class Meta:
        verbose_name = "Director General"  # Nombre singular
        verbose_name_plural = "Directores Generales"  # Nombre plural

    # Método especial para representar el objeto como una cadena (nombre del director general)
    def __str__(self):
        return self.nombre


# Modelo que representa un producto fabricado por un laboratorio
class Producto(models.Model):
    # Campo de texto para el nombre del producto (máximo 100 caracteres)
    nombre = models.CharField(max_length=100)
    # Relación muchos a uno con el modelo Laboratorio
    # Si se elimina un laboratorio, también se eliminan sus productos asociados (on_delete=models.CASCADE)
    laboratorio = models.ForeignKey(
        Laboratorio, on_delete=models.CASCADE, related_name="productos"
    )
    # Campo de fecha para la fecha de fabricación del producto
    # Incluye un validador que asegura que la fecha sea posterior al 1 de enero de 2015
    f_fabricacion = models.DateField(
        validators=[MinValueValidator(limit_value=timezone.datetime(2015, 1, 1).date())]
    )
    # Campo decimal para el precio de costo del producto
    p_costo = models.DecimalField(max_digits=10, decimal_places=2)
    # Campo decimal para el precio de venta del producto
    p_venta = models.DecimalField(max_digits=10, decimal_places=2)
