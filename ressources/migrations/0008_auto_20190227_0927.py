# Generated by Django 2.1.7 on 2019-02-27 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ressources', '0007_auto_20190227_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='oral',
            name='ext',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='ressource',
            name='categorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ressources.Categorie', verbose_name='catégorie'),
        ),
        migrations.AlterField(
            model_name='ressource',
            name='mots_cles',
            field=models.ManyToManyField(to='ressources.MotCle', verbose_name='mots-clés'),
        ),
        migrations.AlterField(
            model_name='ressource',
            name='sous_cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ressources.SousCategorie', verbose_name='sous-catégorie'),
        ),
        migrations.AlterField(
            model_name='souscategorie',
            name='cat_parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ressources.Categorie', verbose_name='catégorie'),
        ),
    ]
