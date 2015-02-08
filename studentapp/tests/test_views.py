from django.test import TestCase, Client


class HomePageTest(TestCase):
    def test_homepage_is_available(self):
        c = Client()
        response = c.get('/')
        self.assertEquals(response.status_code, 200)