from django.contrib import admin
from utilitycosts.models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name')

admin.site.register(Category , CategoryAdmin)


class WaterAdmin(admin.ModelAdmin):
    list_display = ('target_year' , 'target_month' , 'cost' , 'payment_date' , )

admin.site.register(Water , WaterAdmin)


class GasAdmin(admin.ModelAdmin):
    list_display = ('target_year' ,'target_month' , 'cost' , 'payment_date' , )

admin.site.register(Gas , GasAdmin)


class ElectricityAdmin(admin.ModelAdmin):
    list_display = ('target_year' ,'target_month' , 'cost' , 'payment_date' , )

admin.site.register(Electricity , ElectricityAdmin)
