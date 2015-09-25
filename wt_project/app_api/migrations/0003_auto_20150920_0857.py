# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0002_auto_20150911_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiauthenticationkey',
            name='service',
            field=models.CharField(max_length=20, choices=[('facebook', 'facebook'), ('twitter', 'twitter')]),
        ),
    ]
