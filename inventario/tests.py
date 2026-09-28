from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Bodega, Producto, Stock


class StockCreateViewTests(TestCase):
	def test_authenticated_user_can_add_stock(self):
		user = get_user_model().objects.create_user(username="tester", password="test-pass-123")
		self.client.force_login(user)
		producto = Producto.objects.create(sku="SKU-1", nombre="Teclado")
		bodega = Bodega.objects.create(nombre="Central")

		response = self.client.post(
			reverse("inventario:stock_create"),
			{"producto": producto.pk, "bodega": bodega.pk, "cantidad": 4},
		)

		self.assertRedirects(response, reverse("inventario:stock_list"))
		self.assertEqual(Stock.objects.get().cantidad, 4)
