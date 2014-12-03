# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.db import models

from students import Student
# Create your models here.

class Group(models.Model):
    class Meta:
        verbose_name = u'Груп'
        verbose_name_plural = u'Групи'
    name_group = models.CharField(
        max_length=50,
        verbose_name=u'Назва групи')
    king_group = models.ForeignKey(Student,
        verbose_name=u'Староста групи',
        blank=True,
        null=True,
        on_delete=models.SET_NULL)
    def __unicode__(self):
        return u'%s' % (self.name_group)