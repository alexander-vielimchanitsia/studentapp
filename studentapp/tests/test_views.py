from django.test import TestCase, Client

from studentapp.views.students import students_list


class HomePageTest(TestCase):
    def test_homepage_is_available(self):
        c = Client()
        response = c.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_student_func(self):
        pass