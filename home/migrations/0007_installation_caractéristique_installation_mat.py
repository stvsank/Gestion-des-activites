# Generated by Django 4.1.2 on 2022-10-30 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_employe_jours_routeur_antenne'),
    ]

    operations = [
        migrations.AddField(
            model_name='installation',
            name='caractéristique',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='installation',
            name='mat',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
