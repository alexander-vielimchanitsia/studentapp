from django.core.files import File
from django.core.management import call_command
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

        # test for successful command execution if there is group and students
        out = StringIO()
        call_command('students_of_group', 'Group', stdout=out)
        self.assertIn('Luc Besson', out.getvalue())

        # if no group
        out_not_group = StringIO()
        call_command('students_of_group', 'Test', stdout=out_not_group)
        self.assertIn('Group "Test" does not exist', out_not_group.getvalue())

        # if no students in the group
        out_not_stud = StringIO()
        Group.objects.create(name_group='Test 1')
        call_command('students_of_group', 'Test 1', stdout=out_not_stud)
        self.assertIn('No students in group "Test 1"', out_not_stud.getvalue())
        self.assertNotIn('All students in the group "Test 1":',
            out_not_stud.getvalue())

        # purge files after successful tests
        student.foto.delete()