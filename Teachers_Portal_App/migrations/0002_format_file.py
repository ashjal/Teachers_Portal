# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Teachers_Portal_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='format',
            name='file',
            field=models.FileField(default=datetime.datetime(2015, 3, 29, 16, 54, 43, 326000, tzinfo=utc), upload_to=b''),
            preserve_default=False,
        ),
    ]
