# Generated by Django 3.1.2 on 2020-11-18 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20201117_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.customer', verbose_name='покупатель'),
        ),
    ]
