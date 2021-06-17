# Generated by Django 2.2.4 on 2021-05-21 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default=None, max_length=60)),
                ('vaccine', models.CharField(default=None, max_length=60)),
                ('applied_doses', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('person',),
            },
        ),
    ]
