# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_group', models.CharField(max_length=50, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0 \xd0\xb3\xd1\x80\xd1\x83\xd0\xbf\xd0\xb8')),
            ],
            options={
                'verbose_name': '\u0413\u0440\u0443\u043f\u0438',
                'verbose_name_plural': '\u0413\u0440\u0443\u043f\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=15, verbose_name=b'\xd0\x86\xd0\xbc\xd1\x8f')),
                ('last_name', models.CharField(max_length=15, verbose_name=b'\xd0\x9f\xd1\x80\xd1\x96\xd0\xb7\xd0\xb2\xd0\xb8\xd1\x89\xd0\xb5')),
                ('middle_name', models.CharField(max_length=15, verbose_name=b'\xd0\x9f\xd0\xbe \xd0\xb1\xd0\xb0\xd1\x82\xd1\x8c\xd0\xba\xd0\xbe\xd0\xb2\xd1\x96')),
                ('date', models.DateField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbd\xd0\xb0\xd1\x80\xd0\xbe\xd0\xb4\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xbd\xd1\x8f')),
                ('foto', models.FileField(upload_to=b'photos', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe')),
                ('stud_bilet', models.CharField(max_length=100, verbose_name=b'\xd0\xa1\xd1\x82\xd1\x83\xd0\xb4.\xd0\xb1\xd1\x96\xd0\xbb\xd0\xb5\xd1\x82')),
                ('stud_group', models.ForeignKey(verbose_name=b'\xd0\x93\xd1\x80\xd1\x83\xd0\xbf\xd0\xb0', to='studentapp.Group')),
            ],
            options={
                'verbose_name': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442\u0438',
                'verbose_name_plural': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='group',
            name='king_group',
            field=models.ForeignKey(verbose_name=b'\xd0\xa1\xd1\x82\xd0\xb0\xd1\x80\xd0\xbe\xd1\x81\xd1\x82\xd0\xb0 \xd0\xb3\xd1\x80\xd1\x83\xd0\xbf\xd0\xb8', blank=True, to='studentapp.Student', null=True),
            preserve_default=True,
        ),
    ]
