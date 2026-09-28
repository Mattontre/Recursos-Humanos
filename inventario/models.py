from django.db import models

from django.db import models
from django.core.validators import MinValueValidator


class Bodega(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    ubicacion = models.CharField(max_length=200, blank=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    # Ficha técnica
    sku = models.CharField("SKU", max_length=30, unique=True)
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    marca = models.CharField(max_length=80, blank=True)
    modelo = models.CharField(max_length=80, blank=True)
    unidad_medida = models.CharField(max_length=20, default="unidad")
    peso_kg = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True,
                                  validators=[MinValueValidator(0)])
    # Optimización de stock
    stock_minimo = models.PositiveIntegerField(default=0)
    stock_maximo = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.sku} - {self.nombre}"


class Stock(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT, related_name="stocks")
    bodega = models.ForeignKey(Bodega, on_delete=models.PROTECT, related_name="stocks")
    cantidad = models.PositiveIntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["producto", "bodega"], name="stock_unico_por_bodega")
        ]

    def __str__(self):
        return f"{self.producto} @ {self.bodega}: {self.cantidad}"
