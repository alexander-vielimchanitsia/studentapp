# -*- coding: utf-8 -*- 
from django.apps import AppConfig


class StudentsAppConfig(AppConfig):
    name = 'studentapp'
    verbose_name = u'База Студентів'

    def ready(self):
        from studentapp import signals