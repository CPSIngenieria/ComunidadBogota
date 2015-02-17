# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ruperton', '0003_sorteo_id_lista_correo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sorteo',
            name='fecha_cierre_registro_compras',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='sorteo',
            name='fecha_inicio_registro_compras',
            field=models.DateField(),
        ),
    ]
