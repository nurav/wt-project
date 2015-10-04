# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150927_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='user',
        ),
        migrations.AddField(
            model_name='trigger',
            name='variable_mapping',
            field=models.TextField(default=''),
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
