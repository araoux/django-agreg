# Generated by Django 2.1.7 on 2019-02-27 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ressources', '0003_auto_20190227_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='oral',
            name='nom',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
