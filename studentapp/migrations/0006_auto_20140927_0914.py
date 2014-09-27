# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0005_auto_20140927_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='foto',
            field=models.FileField(upload_to=b''),
        ),
    ]
