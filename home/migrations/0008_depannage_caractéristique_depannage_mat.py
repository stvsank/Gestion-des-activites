# Generated by Django 4.1.2 on 2022-10-31 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_installation_caractéristique_installation_mat'),
    ]

    operations = [
        migrations.AddField(
            model_name='depannage',
            name='caractéristique',
            field=models.ImageField(null=True, upload_to='caracteristique'),
        ),
        migrations.AddField(
            model_name='depannage',
            name='mat',
            field=models.ImageField(null=True, upload_to='mat'),
        ),
    ]
