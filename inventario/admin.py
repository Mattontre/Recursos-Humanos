from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Bodega, Producto, Stock

admin.site.register([Bodega, Producto, Stock])