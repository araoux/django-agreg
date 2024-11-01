# Generated by Django 2.1.7 on 2019-03-05 15:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inscriptions_agreg', '0002_inscription'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='centre',
            options={'verbose_name': 'Centres'},
        ),
        migrations.AddField(
            model_name='inscription',
            name='date_inscription',
            field=models.DateField(default=datetime.datetime(2019, 3, 5, 15, 52, 34, 406428, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='centre',
            name='nom',
            field=models.CharField(max_length=30, verbose_name='nom'),
        ),
    ]
