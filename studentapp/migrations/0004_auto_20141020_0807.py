# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0003_auto_20141020_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='king_group',
            field=models.ForeignKey(verbose_name=b'\xd0\xa1\xd1\x82\xd0\xb0\xd1\x80\xd0\xbe\xd1\x81\xd1\x82\xd0\xb0 \xd0\xb3\xd1\x80\xd1\x83\xd0\xbf\xd0\xb8', blank=True, to='studentapp.Student', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='stud_group',
            field=models.ForeignKey(verbose_name=b'\xd0\x93\xd1\x80\xd1\x83\xd0\xbf\xd0\xb0', to='studentapp.Group'),
        ),
    ]
