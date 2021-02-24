from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nsi', '0022_theme_code.py'),
    ]

    operations = [
        migrations.AlterField(
            model_name='td',
            name='contenu',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
