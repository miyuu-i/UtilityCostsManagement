# Generated by Django 3.0.3 on 2021-08-26 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Water',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_month', models.CharField(default=3, max_length=2, verbose_name='月')),
                ('cost', models.IntegerField(verbose_name='料金')),
                ('payment_date', models.DateField(verbose_name='支払日')),
                ('date_to', models.DateField(verbose_name='使用開始日')),
                ('date_from', models.DateField(verbose_name='使用終了日')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilitycosts.Category')),
            ],
            options={
                'verbose_name_plural': '水道代',
            },
        ),
        migrations.CreateModel(
            name='Gas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_month', models.CharField(default=3, max_length=2, verbose_name='月')),
                ('cost', models.IntegerField(verbose_name='料金')),
                ('payment_date', models.DateField(verbose_name='支払日')),
                ('date_to', models.DateField(verbose_name='使用開始日')),
                ('date_from', models.DateField(verbose_name='使用終了日')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilitycosts.Category')),
            ],
            options={
                'verbose_name_plural': 'ガス代',
            },
        ),
        migrations.CreateModel(
            name='Electricity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_month', models.CharField(default=3, max_length=2, verbose_name='月')),
                ('cost', models.IntegerField(verbose_name='料金')),
                ('payment_date', models.DateField(verbose_name='支払日')),
                ('date_to', models.DateField(verbose_name='使用開始日')),
                ('date_from', models.DateField(verbose_name='使用終了日')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilitycosts.Category')),
            ],
            options={
                'verbose_name_plural': '電気代',
            },
        ),
    ]