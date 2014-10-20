# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0002_auto_20141020_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='stud_group',
            field=models.ForeignKey(related_name=b'\xd0\x93\xd1\x80\xd1\x83\xd0\xbf\xd0\xb0', to='studentapp.Group'),
        ),
    ]
