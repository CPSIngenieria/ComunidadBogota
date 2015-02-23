# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ruperton', '0002_auto_20150220_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='monto',
            field=models.CharField(max_length=100),
        ),
    ]
