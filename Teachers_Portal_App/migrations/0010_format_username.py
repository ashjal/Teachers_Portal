# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Teachers_Portal_App', '0009_remove_format_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='format',
            name='username',
            field=models.CharField(default=datetime.datetime(2015, 3, 31, 19, 22, 52, 507000, tzinfo=utc), max_length=40),
            preserve_default=False,
        ),
    ]
