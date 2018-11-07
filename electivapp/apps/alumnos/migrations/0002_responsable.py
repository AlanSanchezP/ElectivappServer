# Generated by Django 2.0.9 on 2018-11-07 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=20)),
                ('alumno', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='alumnos.Alumno')),
            ],
        ),
    ]