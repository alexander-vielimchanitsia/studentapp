# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0003_auto_20150210_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='king_group',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='studentapp.Student', verbose_name='\u0421\u0442\u0430\u0440\u043e\u0441\u0442\u0430 \u0433\u0440\u0443\u043f\u0438'),
        ),
    ]
