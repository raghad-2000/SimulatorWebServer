# Generated by Django 5.0 on 2023-12-19 16:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.DecimalField(decimal_places=8, max_digits=10)),
                ('y', models.DecimalField(decimal_places=8, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Fire',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('startDate', models.DateTimeField(auto_now_add=True)),
                ('state', models.CharField(choices=[('A', 'Actif'), ('E', 'Eteint'), ('I', 'En intervention')], default='A')),
                ('coord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Simulator.coord')),
            ],
        ),
    ]