# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0008_auto_20140930_1642'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': '\u0413\u0440\u0443\u043f\u0438', 'verbose_name_plural': '\u0413\u0440\u0443\u043f\u0438'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442\u0438', 'verbose_name_plural': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442\u0438'},
        ),
        migrations.RemoveField(
            model_name='group',
            name='student',
        ),
        migrations.AlterField(
            model_name='group',
            name='king_group',
            field=models.ForeignKey(verbose_name=b'\xd0\xa1\xd1\x82\xd0\xb0\xd1\x80\xd0\xbe\xd1\x81\xd1\x82\xd0\xb0 \xd0\xb3\xd1\x80\xd1\x83\xd0\xbf\xd0\xb8', to='studentapp.Student'),
        ),
        migrations.AlterField(
            model_name='group',
            name='name_group',
            field=models.CharField(max_length=50, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0 \xd0\xb3\xd1\x80\xd1\x83\xd0\xbf\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='student',
            name='date',
            field=models.DateField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbd\xd0\xb0\xd1\x80\xd0\xbe\xd0\xb4\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xbd\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=15, verbose_name=b'\xd0\x86\xd0\xbc\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='student',
            name='foto',
            field=models.FileField(upload_to=b'photos', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe'),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=15, verbose_name=b'\xd0\x9f\xd1\x80\xd1\x96\xd0\xb7\xd0\xb2\xd0\xb8\xd1\x89\xd0\xb5'),
        ),
        migrations.AlterField(
            model_name='student',
            name='middle_name',
            field=models.CharField(max_length=15, verbose_name=b'\xd0\x9f\xd0\xbe \xd0\xb1\xd0\xb0\xd1\x82\xd1\x8c\xd0\xba\xd0\xbe\xd0\xb2\xd1\x96'),
        ),
        migrations.AlterField(
            model_name='student',
            name='stud_bilet',
            field=models.CharField(max_length=100, verbose_name=b'\xd0\xa1\xd1\x82\xd1\x83\xd0\xb4.\xd0\xb1\xd1\x96\xd0\xbb\xd0\xb5\xd1\x82'),
        ),
        migrations.AlterField(
            model_name='student',
            name='stud_group',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x93\xd1\x80\xd1\x83\xd0\xbf\xd0\xb0'),
        ),
    ]
