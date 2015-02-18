# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('establecimiento', models.CharField(max_length=255)),
                ('monto', models.PositiveIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Concursante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('establecimiento', models.CharField(max_length=255)),
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
            name='Ganador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('foto', models.ImageField(upload_to=b'fotos_ganadores')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('establecimiento', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Residente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('cedula', models.CharField(max_length=100)),
                ('correo', models.EmailField(unique=True, max_length=75)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sorteo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado_sorteo', models.CharField(default=b'Jugando', max_length=50, choices=[(b'Jugando', b'En juego'), (b'Cerrado', b'Cerrado')])),
                ('nombre', models.CharField(max_length=100)),
                ('id_lista_correo', models.CharField(max_length=100)),
                ('fecha_inicio_registro_compras', models.DateField()),
                ('fecha_cierre_registro_compras', models.DateField()),
                ('fecha_sorteo_1', models.DateField(blank=True)),
                ('estado_sorteo_1', models.CharField(default=b'Jugando', max_length=50, choices=[(b'Jugando', b'En juego'), (b'Cerrado', b'Cerrado')])),
                ('premio_sorteo_1', models.CharField(max_length=20)),
                ('numero_ganador_1_sorteo_1', models.PositiveIntegerField(null=True, blank=True)),
                ('numero_ganador_2_sorteo_1', models.PositiveIntegerField(null=True, blank=True)),
                ('numero_ganador_3_sorteo_1', models.PositiveIntegerField(null=True, blank=True)),
                ('fecha_sorteo_2', models.DateField(blank=True)),
                ('estado_sorteo_2', models.CharField(default=b'Jugando', max_length=50, choices=[(b'Jugando', b'En juego'), (b'Cerrado', b'Cerrado')])),
                ('premio_sorteo_2', models.CharField(max_length=20)),
                ('numero_ganador_1_sorteo_2', models.PositiveIntegerField(null=True, blank=True)),
                ('numero_ganador_2_sorteo_2', models.PositiveIntegerField(null=True, blank=True)),
                ('numero_ganador_3_sorteo_2', models.PositiveIntegerField(null=True, blank=True)),
                ('premio_registro_compras', models.CharField(max_length=20)),
                ('ganador_registro_compras', models.ManyToManyField(related_name=b'ganador_sorteo_compras', to='ruperton.Ganador', blank=True)),
                ('ganador_sorteo_1', models.ManyToManyField(related_name=b'ganador_sorteo_1', to='ruperton.Ganador', blank=True)),
                ('ganador_sorteo_2', models.ManyToManyField(related_name=b'ganador_sorteo_2', to='ruperton.Ganador', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ganador',
            name='residente',
            field=models.ForeignKey(to='ruperton.Residente'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='concursante',
            name='residente',
            field=models.ForeignKey(to='ruperton.Residente'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='concursante',
            name='sorteo',
            field=models.ForeignKey(to='ruperton.Sorteo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='compra',
            name='residente',
            field=models.ForeignKey(to='ruperton.Residente'),
            preserve_default=True,
        ),
    ]
