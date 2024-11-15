# Generated by Django 5.1.3 on 2024-11-12 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filament',
            fields=[
                ('filament_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Назва')),
                ('type', models.CharField(max_length=50, verbose_name='Тип')),
                ('color', models.CharField(max_length=50, verbose_name='Колір')),
                ('cost_per_kg', models.FloatField(verbose_name='Вартість філаменту за кг (грн)')),
                ('delivery_cost', models.FloatField(verbose_name='Вартість доставки (грн)')),
                ('spool_weight', models.FloatField(verbose_name='Кількість філаменту на котушці (м)')),
                ('image', models.ImageField(blank=True, null=True, upload_to='filaments/')),
            ],
        ),
        migrations.CreateModel(
            name='GeneralSettings',
            fields=[
                ('general_settings_id', models.AutoField(primary_key=True, serialize=False)),
                ('electricity_cost', models.FloatField(verbose_name='Вартість електроенергії (грн/кВт)')),
                ('rent_cost', models.FloatField(verbose_name='Вартість оренди приміщення (грн/місяць)')),
            ],
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('printer_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Назва')),
                ('cost', models.FloatField(verbose_name='Вартість принтера (грн)')),
                ('description', models.TextField(verbose_name='Опис')),
                ('power_consumption', models.FloatField(verbose_name='Споживання електроенергії (кВт)')),
                ('maintenance_interval', models.IntegerField(verbose_name='Інтервал тех. обслуговування (год)')),
                ('image', models.ImageField(blank=True, null=True, upload_to='printers/')),
            ],
        ),
    ]
