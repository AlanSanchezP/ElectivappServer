# Generated by Django 2.0.9 on 2018-11-07 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('boleta', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('carrera', models.CharField(choices=[('AI', 'Administración Industrial'), ('CC', 'Ciencias de la Informática'), ('II', 'Ingeniería Industrial'), ('IT', 'Ingeniería en Transportes'), ('IN', 'Ingeniería en Informática')], max_length=100)),
                ('estatus', models.BooleanField()),
            ],
        ),
    ]