# Generated by Django 4.1.2 on 2022-10-28 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_employe_jours'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employe',
            name='jours',
        ),
    ]
