from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Stock


class StockListView(LoginRequiredMixin, ListView):
    model = Stock
    template_name = "inventario/stock.html"
    paginate_by = 20

    def get_queryset(self):
        return Stock.objects.select_related("producto", "bodega").order_by("producto__nombre")


class StockCreateView(LoginRequiredMixin, CreateView):
    model = Stock
    fields = ["producto", "bodega", "cantidad"]
    template_name = "inventario/stock_form.html"
    success_url = reverse_lazy("inventario:stock_list")