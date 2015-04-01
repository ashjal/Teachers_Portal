# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Teachers_Portal_App', '0006_auto_20150401_0009'),
    ]

    operations = [
        migrations.AddField(
            model_name='format',
            name='username',
            field=models.CharField(default=None, max_length=40),
            preserve_default=True,
        ),
    ]
