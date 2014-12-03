# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.db import models
# Create your models here.

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