# Generated by Django 4.0.5 on 2022-08-04 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_category_product_image_product_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('con_name', models.CharField(default=' ', max_length=60)),
                ('con_email', models.CharField(default=' ', max_length=60)),
                ('con_phone', models.CharField(default=' ', max_length=10)),
                ('con_desc', models.CharField(default=' ', max_length=500)),
            ],
        ),
    ]
