# Generated by Django 2.2.4 on 2021-06-10 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_auto_20210528_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.DateField(default=None),
        ),
    ]