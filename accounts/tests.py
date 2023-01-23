from django.test import TestCase
from django.urls import reverse

class AccountsTest(TestCase):
    def test_register_url_template(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/register.html")
        
    def test_login_url_template(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")
        
    def test_logout_url(self):
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 302)
    
