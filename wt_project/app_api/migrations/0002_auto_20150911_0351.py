# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiauthenticationkey',
            name='service',
            field=models.CharField(choices=[('twitter', 'twitter'), ('facebook', 'facebook')], max_length=20),
        ),
    ]
