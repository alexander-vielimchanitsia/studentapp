from django.core.files import File
from django.core.management import call_command
from django.core.management.base import CommandError
from django.test import TestCase
from django.utils.six import StringIO

from studentapp.models import Student, Group

class CommandsTestCase(TestCase):
    def create_student(self):
        f = open('studentapp/static/img/foto_icon.png') # photo of student

        return Student.objects.create(
            first_name='Luc',
            last_name='Besson',
            middle_name='Abramovich',
            date='1965-05-27',
            foto=File(f), # save photo in media
            stud_bilet='1234',
            stud_group=Group.objects.create(name_group='Group'))

    def test_students_of_group(self):
        student = self.create_student()
        out = StringIO()

        call_command('students_of_group', 'Group', stdout=out)
        self.assertIn('Luc Besson', out.getvalue())

        student.foto.delete()