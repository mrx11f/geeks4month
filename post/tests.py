from django.test import TestCase, Client 
from django.urls import reverse


class ExamplesTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_contacts_view(self):
        response = self.client.get(reverse("contacts-page"))
        exp_data = "0777 235 246"

        self.assertEqual(response.content.decode(), exp_data)
        self.assertEqual(response.status_code, 200)

    def test_about_view(self):
        response = self.client.get(reverse("about-page"))
        exp_data = "Добро пожаловать на наш сайт!"

        self.assertEqual(response.content.decode(), exp_data)