# Generated by Django 2.1.7 on 2019-02-27 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ressources', '0002_auto_20190227_0001'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='motcle',
            options={'verbose_name': 'Mot-clé'},
        ),
        migrations.AlterModelOptions(
            name='souscategorie',
            options={'verbose_name': 'Sous-catégorie'},
        ),
        migrations.RemoveField(
            model_name='ressource',
            name='type_ressource',
        ),
        migrations.DeleteModel(
            name='TypeRessource',
        ),
    ]
