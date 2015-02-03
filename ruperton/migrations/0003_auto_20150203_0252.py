# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ruperton', '0002_auto_20150203_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sorteo',
            name='numero_ganador_1_fecha_1',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='sorteo',
            name='numero_ganador_1_fecha_2',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='sorteo',
            name='numero_ganador_1_fecha_3',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='sorteo',
            name='numero_ganador_2_fecha_1',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='sorteo',
            name='numero_ganador_2_fecha_2',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='sorteo',
            name='numero_ganador_2_fecha_3',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='sorteo',
            name='numero_ganador_3_fecha_1',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='sorteo',
            name='numero_ganador_3_fecha_2',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='sorteo',
            name='numero_ganador_3_fecha_3',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
