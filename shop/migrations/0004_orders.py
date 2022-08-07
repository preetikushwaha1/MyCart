# Generated by Django 4.0.5 on 2022-08-07 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=1000)),
                ('name', models.CharField(default=' ', max_length=50)),
                ('email', models.CharField(default=' ', max_length=50)),
                ('phone_no', models.CharField(default=' ', max_length=10)),
                ('Address1', models.CharField(default=' ', max_length=150)),
                ('Address2', models.CharField(default=' ', max_length=150)),
                ('city', models.CharField(default=' ', max_length=50)),
                ('state', models.CharField(default=' ', max_length=50)),
                ('zip', models.CharField(default=' ', max_length=50)),
            ],
        ),
    ]
