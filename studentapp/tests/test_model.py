from django.core.files import File

from django.test import TestCase, Client

from studentapp.models import Student, Group


class StudentModelTest(TestCase):
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

    def test_student_creation(self):
        student = self.create_student()

        self.assertTrue(isinstance(student, Student))
        self.assertEqual(student.__unicode__(), '%s %s' %
            (student.first_name, student.last_name))

    def test_student_update(self):
        student = self.create_student()

        f = open('studentapp/static/img/foto.png')

        # updating student
        student.first_name = 'Alexander'
        student.last_name = 'Vielimchanitsia'
        student.middle_name = 'Panasovich'
        student.date = '1997-01-31'
        student.foto = File(f)
        student.stud_bilet = '125'
        student.stud_group = Group.objects.create(name_group='Zick')

        # test update
        self.assertEqual(student.__unicode__(), '%s %s' %
            (student.first_name, student.last_name))

    def test_student_all_fields(self):
        student = self.create_student()

        self.assertEqual(student.first_name, 'Luc')
        self.assertEqual(student.last_name, 'Besson')
        self.assertEqual(student.middle_name, 'Abramovich')
        self.assertEqual(student.date, '1965-05-27')
        self.assertIn('.png', student.foto.path)
        self.assertEqual(student.stud_bilet, '1234')
        self.assertEqual(student.stud_group,
            Group.objects.get(name_group='Name group'))

    def test_student_delete(self):
        student = self.create_student()

        self.assertIn(student, Student.objects.all())

        student.delete()

        self.assertNotIn(student, Student.objects.all())