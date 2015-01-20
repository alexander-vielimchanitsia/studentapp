# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

import logging
logging.basicConfig(format = u'[%(asctime)s]  %(message)s',
    level = logging.INFO, filename = u'students.log')


class Student(models.Model):

    class Meta:
        verbose_name = u'Студент'
        verbose_name_plural = u'Студенти'

    first_name = models.CharField(
        max_length=15,
        verbose_name=u'Імя')

    last_name = models.CharField(
        max_length=15,
        verbose_name=u'Прізвище')

    middle_name = models.CharField(
        max_length=15,
        verbose_name=u'По батькові')

    date = models.DateField(
        verbose_name=u'Дата народження')

    foto = models.ImageField(
        upload_to='photos',
        verbose_name=u'Фото')

    stud_bilet = models.CharField(
        max_length=100,
        verbose_name=u'Студ.білет')

    stud_group = models.ForeignKey('Group',
        verbose_name=u'Група',
        on_delete=models.PROTECT )

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

# @receiver(post_save, sender=Student)
def student_save_handler(sender, **kwargs):
    # logr.debug('Зміни в таблиці студентів: %s, %s' % (sender, kwargs))

    if kwargs['created']:
        details_text = u'Студент був створений'
    else:
        details_text = u'Студент був відредагований'

    s_id = u'id студента: %s' % kwargs['instance'].id
    s_name = u'Повне ім’я студента: %s %s' % (kwargs['instance'].first_name,
        kwargs['instance'].last_name)

    logging.info( '%s, %s, %s' % (details_text, s_id, s_name))

post_save.connect(student_save_handler)