from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
"""
class Costs(models.Model):
    month = models.CharField(max_length=2 ,verbose_name='月', default=3)
    cost = models.IntegerField(verbose_name='料金')
    payment_date = models.DateField(verbose_name='支払日')
    date_to = models.DateField(verbose_name='使用開始日')
    date_from = models.DateField(verbose_name='使用終了日')
    category = models.ForeignKey(Category , on_delete=models.CASCADE)

    def __str__(self):
        return self.month + "月分"

    class Meta:
        verbose_name_plural = ('料金')
"""
class Water(models.Model):
    target_year =  models.CharField(max_length=4 ,verbose_name='年')
    target_month = models.CharField(max_length=2 ,verbose_name='月')
    cost = models.IntegerField(verbose_name='料金')
    payment_date = models.DateField(verbose_name='支払日')
    date_to = models.DateField(verbose_name='使用開始日' , null=True)
    date_from = models.DateField(verbose_name='使用終了日' , null=True)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = ('水道代')

class Gas(models.Model):
    target_year =  models.CharField(max_length=4 ,verbose_name='年')
    target_month = models.CharField(max_length=2 ,verbose_name='月')
    cost = models.IntegerField(verbose_name='料金')
    payment_date = models.DateField(verbose_name='支払日')
    date_to = models.DateField(verbose_name='使用開始日' , null=True)
    date_from = models.DateField(verbose_name='使用終了日' , null=True)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = ('ガス代')

class Electricity(models.Model):
    target_year =  models.CharField(max_length=4 ,verbose_name='年')
    target_month = models.CharField(max_length=2 ,verbose_name='月')
    cost = models.IntegerField(verbose_name='料金')
    payment_date = models.DateField(verbose_name='支払日')
    date_to = models.DateField(verbose_name='使用開始日' , null=True)
    date_from = models.DateField(verbose_name='使用終了日' , null=True)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = ('電気代')
