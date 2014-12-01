# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.db import models
from django import forms

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length = 15, verbose_name = 'Імя')
    last_name = models.CharField(max_length = 15, verbose_name = 'Прізвище')
    middle_name = models.CharField(max_length = 15, verbose_name = 'По батькові')
    date = models.DateField(verbose_name = 'Дата народження')
    foto = models.ImageField(upload_to = 'photos', verbose_name = 'Фото')
    stud_bilet = models.CharField(max_length = 100, verbose_name = 'Студ.білет')
    stud_group = models.ForeignKey('Group', verbose_name = 'Група', on_delete=models.PROTECT )
    class Meta:
            verbose_name = 'Студенти'
            verbose_name_plural = 'Студенти'
    def __unicode__(self):
        return self.last_name + ' ' + self.first_name
    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})


class Group(models.Model):
    name_group = models.CharField(max_length = 50, verbose_name = 'Назва групи')
    king_group = models.ForeignKey(Student, verbose_name = 'Староста групи', blank = True, null = True, on_delete=models.SET_NULL)
    class Meta:
        verbose_name = 'Групи'
        verbose_name_plural = 'Групи'
    def __unicode__(self):
        return self.name_group