# Generated by Django 4.1.2 on 2022-10-31 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_installation_caractéristique_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employe',
            name='profil',
            field=models.ImageField(null=True, upload_to='profil'),
        ),
    ]