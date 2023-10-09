# Generated by Django 3.2.21 on 2023-10-09 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(blank=True, max_length=200)),
                ('edad', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Biblioteca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('puntos', models.FloatField(db_column='puntos_biblioteca', default=5.0)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('tipo', models.CharField(choices=[('ES', 'Español'), ('EN', 'Inglés'), ('FR', 'Francés'), ('IT', 'Italiano')], default='ES', max_length=2)),
                ('descripcion', models.TextField()),
                ('fecha_publicacion', models.DateField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.autor')),
                ('biblioteca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.biblioteca')),
            ],
        ),
        migrations.CreateModel(
            name='DatosCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.TextField()),
                ('gustos', models.TextField()),
                ('telefono', models.IntegerField()),
                ('cliente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.cliente')),
            ],
        ),
    ]
