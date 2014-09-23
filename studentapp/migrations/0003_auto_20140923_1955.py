# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0002_stud_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='foto',
            field=models.FileField(upload_to=None),
        ),
    ]
