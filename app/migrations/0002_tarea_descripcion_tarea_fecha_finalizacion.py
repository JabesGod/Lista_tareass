# Generated by Django 5.1 on 2024-08-18 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tarea',
            name='fecha_finalizacion',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
