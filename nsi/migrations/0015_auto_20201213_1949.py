# Generated by Django 3.1.3 on 2020-12-13 08:49

from django.db import migrations, models
import nsi.models


class Migration(migrations.Migration):

    dependencies = [
        ('nsi', '0014_theme_short_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='short_name',
            field=models.CharField(default=nsi.models.Theme.__str__, max_length=100),
        ),
    ]
