# Generated by Django 3.1.2 on 2020-11-10 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nsi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='niveau',
            field=models.CharField(choices=[('P', 'Première'), ('T', 'Terminale'), ('A', 'Autre')], default='P', max_length=1),
        ),
    ]
