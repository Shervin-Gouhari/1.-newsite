from django.test import SimpleTestCase

class PagesTest(SimpleTestCase):
    def test_home_url_template(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/home.html")
    
    def test_about_url_template(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/about.html")