# Generated by Django 2.2.4 on 2021-05-21 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('place', '0001_initial'),
        ('person', '0001_initial'),
        ('list_information', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listinformation',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='person.Person'),
        ),
        migrations.AddField(
            model_name='listinformation',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='place.Place'),
        ),
    ]
