# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_group', models.CharField(max_length=50, verbose_name='\u041d\u0430\u0437\u0432\u0430 \u0433\u0440\u0443\u043f\u0438')),
            ],
            options={
                'verbose_name': '\u0413\u0440\u0443\u043f',
                'verbose_name_plural': '\u0413\u0440\u0443\u043f\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=15, verbose_name='\u0406\u043c\u044f')),
                ('last_name', models.CharField(max_length=15, verbose_name='\u041f\u0440\u0456\u0437\u0432\u0438\u0449\u0435')),
                ('middle_name', models.CharField(max_length=15, verbose_name='\u041f\u043e \u0431\u0430\u0442\u044c\u043a\u043e\u0432\u0456')),
                ('date', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u043d\u0430\u0440\u043e\u0434\u0436\u0435\u043d\u043d\u044f')),
                ('foto', models.ImageField(upload_to=b'photos', verbose_name='\u0424\u043e\u0442\u043e')),
                ('stud_bilet', models.CharField(max_length=100, verbose_name='\u0421\u0442\u0443\u0434.\u0431\u0456\u043b\u0435\u0442')),
                ('stud_group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u0413\u0440\u0443\u043f\u0430', to='studentapp.Group')),
            ],
            options={
                'verbose_name': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442',
                'verbose_name_plural': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='group',
            name='king_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u0421\u0442\u0430\u0440\u043e\u0441\u0442\u0430 \u0433\u0440\u0443\u043f\u0438', blank=True, to='studentapp.Student', null=True),
            preserve_default=True,
        ),
    ]
