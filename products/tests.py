from django.test import TestCase
from django.urls import reverse

from .models import Product

# Create your tests here.
class productListViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/productos/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('list_products'))
        self.assertEqual(response.status_code, 200)

    def test_product_listview_count(self):
        response = self.client.get(reverse('list_products'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['products'].count(), 0)

    def test_product_listview_count_1(self):
        Product.objects.create(
          name='Product 1', 
          description='Description 1',
          price=1000,
          available=True
        )
        response = self.client.get(reverse("list_products"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['products'].count(), 1)
