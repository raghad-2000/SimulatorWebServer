from django.contrib import admin

# Register your models here.
from .models import Sensor

admin.site.register(Sensor)