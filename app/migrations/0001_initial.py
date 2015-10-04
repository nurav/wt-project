# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='APIAuthenticationKey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('service', models.CharField(choices=[('twitter', 'twitter'), ('facebook', 'facebook')], max_length=20)),
                ('auth_data', models.TextField()),
                ('user', models.ForeignKey(related_name='api_auth_keys', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trigger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(max_length=50)),
                ('event', models.CharField(max_length=50)),
                ('script', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('user', models.ForeignKey(related_name='triggers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='apiauthenticationkey',
            unique_together=set([('user', 'service')]),
        ),
    ]
