# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ruperton', '0008_ganador_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='ganador',
            name='establecimiento',
            field=models.CharField(default='CPS', max_length=100),
            preserve_default=False,
        ),
    ]
