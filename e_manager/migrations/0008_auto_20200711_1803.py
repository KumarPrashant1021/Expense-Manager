# Generated by Django 3.0.6 on 2020-07-11 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_manager', '0007_auto_20200707_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensedetails',
            name='category',
            field=models.CharField(choices=[('Food', 'Food'), ('Social Life', 'Social life'), ('Education', 'Education'), ('Household', 'Household'), ('Transportation', 'Transportation'), ('Fashion', 'Fashion'), ('Health', 'Health'), ('Self Development', 'Self development'), ('Gift', 'Gift'), ('Other', 'Other')], max_length=50),
        ),
    ]
