# Generated by Django 2.2.4 on 2021-06-01 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_information', '0003_auto_20210601_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listinformation',
            name='vaccine',
            field=models.IntegerField(default=0),
        ),
    ]
