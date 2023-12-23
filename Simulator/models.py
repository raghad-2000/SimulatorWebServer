from django.db import models

# Create your models here.

class Fire(models.Model):
    id = models.IntegerField(primary_key=True)
    x_coord = models.DecimalField(max_digits=10, decimal_places=8, default=0)
    y_coord = models.DecimalField(max_digits=10, decimal_places=8, default=0)
    startDate = models.DateTimeField(auto_now_add=True)
    
    class StateEnum(models.TextChoices):
        ON   = 'A', 'Actif'
        OFF   = 'E', 'Eteint',
        ONGOING = 'I', 'En intervention'

    state = models.CharField(choices=StateEnum.choices, default=StateEnum.ON)


class Sensor(models.Model):
    id = models.IntegerField(primary_key=True)
    x_coord = models.DecimalField(max_digits=10, decimal_places=8, default=0)
    y_coord = models.DecimalField(max_digits=10, decimal_places=8, default=0)
    temperature = models.DecimalField(max_digits=10, decimal_places=8, default=0)