# Generated by Django 3.1.3 on 2020-12-24 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nsi', '0020_auto_20201214_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='cours',
            name='image1',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='cours',
            name='image2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='cours',
            name='image3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='cours',
            name='text1',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='cours',
            name='text2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='cours',
            name='text3',
            field=models.TextField(blank=True),
        ),
    ]
