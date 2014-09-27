# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0004_auto_20140924_1730'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Table_group',
            new_name='TableGroup',
        ),
        migrations.RenameField(
            model_name='tablegroup',
            old_name='table_group_student',
            new_name='student',
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=15),
        ),
    ]
