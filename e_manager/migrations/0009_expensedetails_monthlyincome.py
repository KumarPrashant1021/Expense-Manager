# Generated by Django 3.0.6 on 2020-07-16 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_manager', '0008_auto_20200711_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='expensedetails',
            name='monthlyIncome',
            field=models.DecimalField(decimal_places=0, max_digits=15, null=True),
        ),
    ]
