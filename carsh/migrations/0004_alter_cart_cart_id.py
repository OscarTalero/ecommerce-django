# Generated by Django 4.0.2 on 2022-02-22 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carsh', '0003_rename_cars_cart_rename_carsitem_cartitem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]