# Generated by Django 3.1.2 on 2020-10-23 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_auto_20201024_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='lte_exists',
            field=models.BooleanField(null=True),
        ),
    ]
