# Generated by Django 3.1.3 on 2021-06-16 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20210616_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='highest_bid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name='auction',
            name='price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=100),
        ),
        migrations.AlterField(
            model_name='bid',
            name='price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=100),
        ),
    ]
