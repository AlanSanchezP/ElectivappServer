# Generated by Django 2.0.9 on 2018-12-04 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0004_auto_20181108_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipoactividad',
            name='horasRequeridas',
            field=models.PositiveIntegerField(),
        ),
    ]
