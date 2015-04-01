# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Teachers_Portal_App', '0008_auto_20150401_0049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='format',
            name='username',
        ),
    ]
