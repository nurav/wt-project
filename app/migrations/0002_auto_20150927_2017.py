# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(max_length=50)),
                ('event', models.CharField(max_length=50)),
                ('script', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('user', models.ForeignKey(related_name='events', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='trigger',
            name='description',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trigger',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='trigger',
            name='original_user',
            field=models.ForeignKey(related_name='created_trigger', default=0, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='trigger',
            name='shared',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='apiauthenticationkey',
            name='service',
            field=models.CharField(choices=[('twitter', 'Twitter')], max_length=20),
        ),
    ]
