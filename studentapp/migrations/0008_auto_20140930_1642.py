# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0007_auto_20140927_0915'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TableGroup',
            new_name='Group',
        ),
        migrations.AlterField(
            model_name='student',
            name='foto',
            field=models.FileField(upload_to=b'static/upload'),
        ),
    ]
