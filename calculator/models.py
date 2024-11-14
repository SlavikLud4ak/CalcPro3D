# models.py
from django.db import models
from django.core.validators import MinValueValidator

class GeneralSettings (models.Model):
    general_settings_id = models.AutoField(primary_key=True)
    electricity_cost = models.FloatField("Вартість електроенергії (грн/кВт)")
    rent_cost = models.FloatField("Вартість оренди приміщення (грн/місяць)")

    def __str__(self):
        return str(f"ID: {self.id}: {self.electricity_cost}")

class Filament(models.Model):
    filament_id = models.AutoField(primary_key=True)
    name = models.CharField("Назва", max_length=100)
    type = models.CharField("Тип", max_length=50)
    color = models.CharField("Колір", max_length=50)
    cost_per_kg = models.FloatField("Вартість філаменту за кг (грн)")
    delivery_cost = models.FloatField("Вартість доставки (грн)")
    spool_weight = models.FloatField("Кількість філаменту на котушці (м)")
    image = models.ImageField(upload_to='filaments/', blank=True, null=True)

class Printer(models.Model):
    printer_id = models.AutoField(primary_key=True)
    name = models.CharField("Назва", max_length=100)
    cost = models.FloatField("Вартість принтера (грн)")
    description = models.TextField("Опис")
    power_consumption = models.FloatField("Споживання електроенергії (кВт)")
    maintenance_interval = models.IntegerField("Інтервал тех. обслуговування (год)")
    image = models.ImageField(upload_to='printers/', blank=True, null=True)
