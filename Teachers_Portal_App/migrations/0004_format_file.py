# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Teachers_Portal_App', '0003_remove_format_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='format',
            name='file',
            field=models.FileField(upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
