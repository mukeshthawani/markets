# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_auto_20150227_0054'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefinitionTerms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('terms', models.CharField(unique=True, max_length=50)),
                ('full_terms', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='DataChoice',
        ),
    ]
