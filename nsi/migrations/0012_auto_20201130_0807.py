# Generated by Django 3.1.3 on 2020-11-29 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nsi', '0011_theme_imageurl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='imageURL',
        ),
        migrations.AddField(
            model_name='theme',
            name='image',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
