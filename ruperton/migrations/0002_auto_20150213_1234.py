# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ruperton', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sorteo',
            name='ganador_registro_compras',
            field=models.ManyToManyField(related_name=b'ganador_sorteo_compras', to=b'ruperton.Ganador', blank=True),
        ),
        migrations.AlterField(
            model_name='sorteo',
            name='ganador_sorteo_1',
            field=models.ManyToManyField(related_name=b'ganador_sorteo_1', to=b'ruperton.Ganador', blank=True),
        ),
        migrations.AlterField(
            model_name='sorteo',
            name='ganador_sorteo_2',
            field=models.ManyToManyField(related_name=b'ganador_sorteo_2', to=b'ruperton.Ganador', blank=True),
        ),
    ]
