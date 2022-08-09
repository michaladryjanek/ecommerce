# Generated by Django 4.0.4 on 2022-08-06 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_order_complete_alter_product_digital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='digital',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='prices',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
