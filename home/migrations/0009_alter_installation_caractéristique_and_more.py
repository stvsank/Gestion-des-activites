# Generated by Django 4.1.2 on 2022-10-31 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_depannage_caractéristique_depannage_mat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installation',
            name='caractéristique',
            field=models.ImageField(null=True, upload_to='caracteristique'),
        ),
        migrations.AlterField(
            model_name='installation',
            name='mat',
            field=models.ImageField(null=True, upload_to='mat'),
        ),
    ]
