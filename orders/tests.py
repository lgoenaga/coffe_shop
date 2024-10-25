from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
class MyOrdersViewTest(TestCase):
  
    def test_redirect_user_no_logged(self):
        url = reverse('my_orders')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
    
    def test_redirect_user_logged(self):
        User.objects.create_user(username='test', password='12345')
        self.client.login(username='test', password='12345')
        url = reverse('my_orders')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)