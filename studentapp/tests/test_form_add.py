from django.test import TestCase, Client

from studentapp.models import Student, Group


class StudentFormTest(TestCase):
    def test_student_from_submit(self):
        c = Client()

        f = open('studentapp/static/img/foto_icon.png')

        data = {'first_name': 'Alexander',
                'last_name': 'Vielimchanitsia',
                'middle_name': 'Panasovich',
                'date': '1997-01-31',
                'foto': f,
                'stud_bilet': '1234',
                'stud_group': Group.objects.create(name_group='Group')}

        response = c.post('/students/add/', data)
        self.assertEquals(response.status_code, 302)
        form = Student.objects.get(first_name=data['first_name'])