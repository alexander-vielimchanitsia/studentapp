from django.test import TestCase, Client

from studentapp.models import Student, Group
from studentapp.forms import StudentFormAdd, StudentFormEdit


class StudentFormTest(TestCase):
    def test_student_from_submit(self):
        c = Client()
        f = open('studentapp/static/img/foto_icon.png') # photo of student

        data = {'first_name': 'Alexander',
                'last_name': 'Vielimchanitsia',
                'middle_name': 'Panasovich',
                'date': '1997-01-31',
                'foto': f,
                'stud_bilet': '1234',
                'stud_group': Group.objects.create(name_group='Group').id}

        response = c.post('/students/add/', data)
        self.assertEquals(response.status_code, 302)

        # purge files after successful tests
        Student.objects.get(first_name='Alexander').foto.delete()