# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Teachers_Portal_App', '0002_format_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='format',
            name='file',
        ),
    ]
