# Generated by Django 4.2.7 on 2024-01-03 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.PositiveSmallIntegerField(choices=[(1, 'administardor'), (2, 'cliente'), (3, 'bibliotecario')], default=1),
        ),
    ]
