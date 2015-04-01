# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Teachers_Portal_App', '0007_format_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='format',
            name='username',
            field=models.CharField(max_length=40),
            preserve_default=True,
        ),
    ]
