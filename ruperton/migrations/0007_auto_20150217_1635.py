# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ruperton', '0006_auto_20150217_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sorteo',
            name='premio_registro_compras',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='sorteo',
            name='premio_sorteo_1',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='sorteo',
            name='premio_sorteo_2',
            field=models.CharField(max_length=20),
        ),
    ]
