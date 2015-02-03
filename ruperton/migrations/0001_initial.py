# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concursante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=75)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=255)),
                ('establecimiento', models.CharField(max_length=255, blank=True)),
                ('numero_ganador_1', models.PositiveIntegerField()),
                ('numero_ganador_2', models.PositiveIntegerField()),
                ('numero_ganador_3', models.PositiveIntegerField()),
                ('acepto_terminos', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sorteo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_sorteo_1', models.DateField(blank=True)),
                ('fecha_sorteo_2', models.DateField(blank=True)),
                ('fecha_sorteo_3', models.DateField(blank=True)),
                ('premio_fecha_1', models.PositiveIntegerField()),
                ('premio_fecha_2', models.PositiveIntegerField()),
                ('premio_fecha_3', models.PositiveIntegerField()),
                ('numero_ganador_1_fecha_1', models.PositiveIntegerField()),
                ('numero_ganador_2_fecha_1', models.PositiveIntegerField()),
                ('numero_ganador_3_fecha_1', models.PositiveIntegerField()),
                ('numero_ganador_1_fecha_2', models.PositiveIntegerField()),
                ('numero_ganador_2_fecha_2', models.PositiveIntegerField()),
                ('numero_ganador_3_fecha_2', models.PositiveIntegerField()),
                ('numero_ganador_1_fecha_3', models.PositiveIntegerField()),
                ('numero_ganador_2_fecha_3', models.PositiveIntegerField()),
                ('numero_ganador_3_fecha_3', models.PositiveIntegerField()),
                ('estado_fecha_1', models.CharField(default=b'JU', max_length=2, choices=[(b'JU', b'En juego'), (b'EN', b'Entregado'), (b'AC', b'Acumulado')])),
                ('estado_fecha_2', models.CharField(default=b'JU', max_length=2, choices=[(b'JU', b'En juego'), (b'EN', b'Entregado'), (b'AC', b'Acumulado')])),
                ('estado_fecha_3', models.CharField(default=b'JU', max_length=2, choices=[(b'JU', b'En juego'), (b'EN', b'Entregado'), (b'AC', b'Acumulado')])),
                ('estado_sorteo', models.CharField(default=b'IN', max_length=2, choices=[(b'JU', b'En juego'), (b'IN', b'En inscripciones'), (b'CE', b'Cerrado')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='concursante',
            name='sorteo',
            field=models.ForeignKey(to='ruperton.Sorteo'),
            preserve_default=True,
        ),
    ]
