# Generated by Django 4.0.5 on 2022-09-10 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_order_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='ord_amount',
            field=models.IntegerField(default='0'),
        ),
    ]
