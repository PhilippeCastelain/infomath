# Generated by Django 3.1.3 on 2020-12-13 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nsi', '0012_auto_20201130_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='cours',
            name='contenu',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='td',
            name='contenu',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
