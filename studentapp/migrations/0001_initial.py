# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=15)),
                ('middle_name', models.CharField(max_length=15)),
                ('date', models.FileField(upload_to=None)),
                ('foto', models.CharField(max_length=100)),
                ('stud_bilet', models.CharField(max_length=100)),
                ('stud_group', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
