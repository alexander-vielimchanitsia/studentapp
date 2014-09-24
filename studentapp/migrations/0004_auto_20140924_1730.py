# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0003_auto_20140923_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table_group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_group', models.CharField(max_length=50)),
                ('king_group', models.CharField(max_length=50)),
                ('table_group_student', models.ForeignKey(to='studentapp.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Stud_group',
        ),
        migrations.AlterField(
            model_name='student',
            name='stud_group',
            field=models.CharField(max_length=200),
        ),
    ]
