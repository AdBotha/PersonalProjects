# Generated by Django 2.2.2 on 2019-06-28 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geogram', '0008_countries'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='countries',
            options={'ordering': ['name', 'geom']},
        ),
    ]
