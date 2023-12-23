# Generated by Django 5.0 on 2023-12-23 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Simulator', '0004_delete_coord_remove_fire_xcoord_remove_fire_ycoord_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('x_coord', models.DecimalField(decimal_places=8, default=0, max_digits=10)),
                ('y_coord', models.DecimalField(decimal_places=8, default=0, max_digits=10)),
                ('temperature', models.DecimalField(decimal_places=8, default=0, max_digits=10)),
            ],
        ),
    ]
