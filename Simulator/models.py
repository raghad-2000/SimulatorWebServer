from django.db import models

# Create your models here.

class Coord(models.Model):
    x = models.DecimalField(max_digits=10, decimal_places=8)
    y = models.DecimalField(max_digits=10, decimal_places=8)


class Fire(models.Model):
    id = models.IntegerField(primary_key=True)
    coord = models.ForeignKey(Coord, on_delete=models.CASCADE)
    startDate = models.DateTimeField(auto_now_add=True)
    
    class StateEnum(models.TextChoices):
        ON   = 'A', 'Actif'
        OFF   = 'E', 'Eteint',
        ONGOING = 'I', 'En intervention'

    state = models.CharField(choices=StateEnum.choices, default=StateEnum.ON)


