# Generated by Django 3.1.3 on 2020-12-14 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nsi', '0016_remove_theme_short_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='short_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
