# Generated by Django 2.0.9 on 2018-11-06 02:53
from django.db import migrations, models
import django.db.models.deletion
from django.core.management import call_command

fixture = "tipoactividad"

def load_fixture(apps, schema_editor):
    call_command('loaddata', fixture, app_label='actividades') 

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, unique=True, validators=[django.core.validators.RegexValidator(regex="^([A-Za-zÁÉÍÓÚñáéíóúÑ]{0}?[A-Za-zÁÉÍÓÚñáéíóúÑ\\'])+[\\s]?([A-Za-zÁÉÍÓÚñáéíóúÑ]{0}?[A-Za-zÁÉÍÓÚñáéíóúÑ\\'])?$")])),
            ],
        ),
        migrations.CreateModel(
            name='TipoActividad',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150, unique=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actividades.Categoria')),
                ('horasRequeridas', models.PositiveIntegerField(default=20)),
            ],
        ),

        migrations.RunPython(load_fixture),
    ]
