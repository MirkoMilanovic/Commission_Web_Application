# Generated by Django 4.0.4 on 2022-04-13 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReportApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='net_income',
            field=models.FloatField(),
        ),
    ]
