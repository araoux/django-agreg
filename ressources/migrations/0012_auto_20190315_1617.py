# Generated by Django 2.1.7 on 2019-03-15 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ressources', '0011_auto_20190315_1612'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='oral',
            options={'verbose_name': 'Oral', 'verbose_name_plural': 'Oraux'},
        ),
        migrations.AlterModelOptions(
            name='ressourcefichier',
            options={'verbose_name': 'Ressource - pdf', 'verbose_name_plural': 'Ressources - pdf'},
        ),
        migrations.AlterModelOptions(
            name='ressourceimage',
            options={'verbose_name': 'Ressource - Image', 'verbose_name_plural': 'Ressources - Images'},
        ),
        migrations.AlterModelOptions(
            name='ressourcelien',
            options={'verbose_name': 'Ressource - Lien', 'verbose_name_plural': 'Ressources - Liens'},
        ),
        migrations.AlterModelOptions(
            name='ressourcescript',
            options={'verbose_name': 'Ressource - Script Python', 'verbose_name_plural': 'Ressources - Scripts Python'},
        ),
    ]
