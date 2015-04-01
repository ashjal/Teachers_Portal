# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Teachers_Portal_App', '0004_format_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='format',
            name='volume',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='format',
            name='year',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
