from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.views.generic import TemplateView

from inventario.models import Bodega, Producto, Stock


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "inicio/index.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["total_productos"] = Producto.objects.filter(activo=True).count()
        contexto["total_bodegas"] = Bodega.objects.filter(activa=True).count()
        contexto["bajo_minimo"] = Stock.objects.filter(
            cantidad__lt=F("producto__stock_minimo")
        ).count()
        return contexto