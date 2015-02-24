from django.core.files import File
from django.test import TestCase, Client

from studentapp.models import Student, Group


class HomePageTest(TestCase):
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

    def test_view_student_func(self):
        c = Client()
        student = self.create_student()
        response = c.get('/')

        self.assertEquals(response.status_code, 200)

        self.assertIn(student.first_name, response.content)
        self.assertIn('</html>', response.content)

        student.foto.delete()