# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import Teachers_Portal_App.models


class Migration(migrations.Migration):

    dependencies = [
        ('Teachers_Portal_App', '0005_auto_20150329_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='format',
            name='file',
            field=models.FileField(upload_to=Teachers_Portal_App.models.get_upload_file_name),
            preserve_default=True,
        ),
    ]
