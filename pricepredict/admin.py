from django.contrib import admin
from pricepredict.models import BuyCar
# Register your models here.

class buycar(admin.ModelAdmin):
    list_display=('company','car_model','year_of_purchase','fuel_type','kms_driven','predicted_price')


admin.site.register(BuyCar,buycar)