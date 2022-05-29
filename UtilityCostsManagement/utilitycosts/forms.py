from django.forms import ModelForm
from .models import *

class WaterForm(ModelForm):
    """ 水道代のフォーム """
    class Meta:
        model = Water
        fields = ('target_year', 'target_month', 'cost', 'payment_date', 'date_to' , 'date_from' , 'category', )

class GasForm(ModelForm):
    """ ガス代のフォーム """
    class Meta:
        model = Gas
        fields = ('target_year', 'target_month', 'cost', 'payment_date', 'date_to' , 'date_from' , 'category', )

class ElectricityForm(ModelForm):
    """ ガス代のフォーム """
    class Meta:
        model = Electricity
        fields = ('target_year', 'target_month', 'cost', 'payment_date', 'date_to' , 'date_from' , 'category', )
