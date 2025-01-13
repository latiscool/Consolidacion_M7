from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

# Create your models here.


class Laboratorio(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.OneToOneField(
        Laboratorio, on_delete=models.CASCADE, related_name="director"
    )
    especialidad = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Director General"
        verbose_name_plural = "Directores Generales"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.ForeignKey(
        Laboratorio, on_delete=models.CASCADE, related_name="productos"
    )
    f_fabricacion = models.DateField(
        validators=[MinValueValidator(limit_value=timezone.datetime(2015, 1, 1).date())]
    )
    p_costo = models.DecimalField(max_digits=10, decimal_places=2)
    p_venta = models.DecimalField(max_digits=10, decimal_places=2)
