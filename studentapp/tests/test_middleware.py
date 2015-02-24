from django.core.files import File
from django.test import TestCase, Client

from studentapp.middleware import StatsMiddleware
from studentapp.models import Student, Group


class StatsMiddlewareTest(TestCase):
    def setUp(self):
        c = Client()
        self.middleware = StatsMiddleware()
        self.response = c.get('/')

    def create_student(self):
        f = open('studentapp/static/img/foto_icon.png') # photo of student

        return Student.objects.create(
            first_name='Luc',
            last_name='Besson',
            middle_name='Abramovich',
            date='1965-05-27',
            foto=File(f), # save photo in media
            stud_bilet='1234',
            stud_group=Group.objects.create(name_group='Name group'))

    def test_sats_middleware_content(self):
        self.assertTrue(hasattr(self.response, 'content'))
        self.assertTrue(
            self.response.get('Content-Type', '') == 'text/html; charset=utf-8'
            )
        self.assertIn('<ol class="breadcrumb">'
            '<div class="pull-right" id="rendering_page_text">',
            self.response.content)

    def test_middlewate_page_photo(self):
        c = Client()

        self.create_student()

        student = Student.objects.get(first_name='Luc')
        photo_url = student.foto.url

        response = c.get(photo_url)
        self.assertEquals(response.status_code, 200)

        student.foto.delete()