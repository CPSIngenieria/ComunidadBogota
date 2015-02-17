# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ruperton', '0004_auto_20150216_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sorteo',
            name='estado_sorteo_1',
            field=models.CharField(default=b'Jugando', max_length=2, choices=[(b'Jugando', b'En juego'), (b'Cerrado', b'Cerrado')]),
        ),
        migrations.AlterField(
            model_name='sorteo',
            name='estado_sorteo_2',
            field=models.CharField(default=b'Jugando', max_length=2, choices=[(b'Jugando', b'En juego'), (b'Cerrado', b'Cerrado')]),
        ),
    ]
