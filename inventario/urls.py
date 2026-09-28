from django.urls import path
from . import views

app_name = "inventario"
urlpatterns = [
    path("agregar/", views.StockCreateView.as_view(), name="stock_create"),
    path("", views.StockListView.as_view(), name="stock_list"),
]