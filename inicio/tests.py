from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class HomeViewTests(TestCase):
    def test_requires_login(self):
        response = self.client.get(reverse("inicio:home"))
        self.assertEqual(response.status_code, 302)

    def test_authenticated_user_sees_home(self):
        user = get_user_model().objects.create_user(username="tester", password="test-pass-123")
        self.client.force_login(user)
        response = self.client.get(reverse("inicio:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Inventario")