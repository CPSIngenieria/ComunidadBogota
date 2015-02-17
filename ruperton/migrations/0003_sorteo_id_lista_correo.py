# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ruperton', '0002_auto_20150213_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='sorteo',
            name='id_lista_correo',
            field=models.CharField(default=12345, max_length=100),
            preserve_default=False,
        ),
    ]
