# Generated by Django 5.0.6 on 2024-05-30 10:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriesFonction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CategoriesMatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ListeEmploye',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('prenom', models.CharField(max_length=200)),
                ('quartier', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=200)),
                ('fonction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Apps.categoriesfonction')),
            ],
        ),
        migrations.CreateModel(
            name='MaterielsOBM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.IntegerField(default=1)),
                ('nomProduits', models.CharField(max_length=200)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('desc', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Apps.categoriesmatos')),
            ],
            options={
                'ordering': ['-creation_date'],
            },
        ),
        migrations.CreateModel(
            name='SortiDuMatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.IntegerField(default=1)),
                ('sortie_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Apps.categoriesmatos')),
                ('nom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Apps.materielsobm')),
                ('nomAgentsAyantPris', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='Apps.listeemploye')),
            ],
            options={
                'ordering': ['-sortie_date'],
            },
        ),
        migrations.CreateModel(
            name='MatosRendu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.IntegerField(default=1)),
                ('retour_date', models.DateTimeField(auto_now_add=True)),
                ('etat', models.TextField(default='1')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Apps.categoriesmatos')),
                ('nomProduits', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Apps.materielsobm')),
                ('agentsAyantretour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Apps.sortidumatos')),
            ],
            options={
                'ordering': ['-retour_date'],
            },
        ),
    ]