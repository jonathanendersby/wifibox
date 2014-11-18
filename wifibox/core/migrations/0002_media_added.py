# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='added',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 18, 5, 13, 4, 789639, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
