# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0004_auto_20141020_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='foto',
            field=models.ImageField(upload_to=b'photos', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe'),
        ),
    ]
