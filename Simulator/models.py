from django.db import models

# Create your models here.

class Fire(models.Model):
    id = models.IntegerField(primary_key=True)
    lat = models.DecimalField(max_digits=10, decimal_places=8, default=0)
    lon = models.DecimalField(max_digits=10, decimal_places=8, default=0)
    startDate = models.DateTimeField(auto_now_add=True)
    
    class StateEnum(models.TextChoices):
        ON   = 'A', 'Actif'
        OFF   = 'E', 'Eteint',
        ONGOING = 'I', 'En intervention'

    state = models.CharField(choices=StateEnum.choices, default=StateEnum.ON)

class Sensor(models.Model):
    id = models.IntegerField(primary_key=True)
    lat = models.DecimalField(max_digits=10, decimal_places=8, default=0)
    lon = models.DecimalField(max_digits=10, decimal_places=8, default=0)
    
class SensorReading(models.Model):
    sensor = models.OneToOneField(
        Sensor,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    data = models.DecimalField(max_digits=10, decimal_places=8, default=0)
    readingDate = models.DateTimeField(auto_now_add=True)