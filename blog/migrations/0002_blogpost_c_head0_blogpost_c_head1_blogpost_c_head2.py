# Generated by Django 4.0.5 on 2022-09-04 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='c_head0',
            field=models.CharField(default=' ', max_length=5000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='c_head1',
            field=models.CharField(default=' ', max_length=5000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='c_head2',
            field=models.CharField(default=' ', max_length=5000),
        ),
    ]
