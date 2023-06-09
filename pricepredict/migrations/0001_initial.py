# Generated by Django 4.1.5 on 2023-02-25 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuyCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50)),
                ('car_model', models.CharField(max_length=50)),
                ('year_of_purchase', models.BigIntegerField()),
                ('fuel_type', models.CharField(max_length=50)),
                ('kms_driven', models.BigIntegerField()),
                ('predicted_price', models.BigIntegerField()),
            ],
        ),
    ]
