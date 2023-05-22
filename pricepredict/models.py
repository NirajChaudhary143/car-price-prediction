from django.db import models

# Create your models here.
class BuyCar(models.Model):
    company=models.CharField(max_length=50)
    car_model=models.CharField(max_length=50)
    year_of_purchase=models.BigIntegerField()
    fuel_type=models.CharField(max_length=50)
    kms_driven=models.BigIntegerField()
    predicted_price=models.BigIntegerField()