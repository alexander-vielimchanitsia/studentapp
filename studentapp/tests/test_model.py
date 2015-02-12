from django.test import TestCase, Client

from studentapp.models import Student, Group


class StudentModelTest(TestCase):
    def test_student_model_add(self):
        f = open('studentapp/static/img/foto_icon.png') # photo of student

        Group.objects.create(name_group='Name group')

        Student.objects.create(first_name='Luc',
                                last_name='Besson',
                                middle_name='Abramovich',
                                date='1965-05-27',
                                foto=f,
                                stud_bilet='1234',
                                stud_group=Group.objects.get(name_group='Name group').id)

