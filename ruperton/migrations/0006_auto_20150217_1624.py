# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ruperton', '0005_auto_20150217_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sorteo',
            name='estado_sorteo_1',
            field=models.CharField(default=b'Jugando', max_length=50, choices=[(b'Jugando', b'En juego'), (b'Cerrado', b'Cerrado')]),
        ),
        migrations.AlterField(
            model_name='sorteo',
            name='estado_sorteo_2',
            field=models.CharField(default=b'Jugando', max_length=50, choices=[(b'Jugando', b'En juego'), (b'Cerrado', b'Cerrado')]),
        ),
    ]
