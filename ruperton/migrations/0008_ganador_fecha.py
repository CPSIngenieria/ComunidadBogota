# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ruperton', '0007_auto_20150217_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='ganador',
            name='fecha',
            field=models.DateField(default=datetime.date(2015, 2, 17), auto_now_add=True),
            preserve_default=False,
        ),
    ]
