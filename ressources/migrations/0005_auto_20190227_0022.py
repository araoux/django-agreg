# Generated by Django 2.1.7 on 2019-02-27 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ressources', '0004_oral_nom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oral',
            name='typeOral',
        ),
        migrations.AddField(
            model_name='oral',
            name='type_oral',
            field=models.CharField(choices=[('LC', 'Leçon de chimie'), ('LP', 'Leçon de physique'), ('M', 'Montage'), ('Dr', 'Mise en perspective didactique')], default=1, max_length=2),
            preserve_default=False,
        ),
    ]
