# Generated by Django 2.2.2 on 2019-06-22 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geogram', '0005_auto_20190621_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pindrop',
            name='pinphoto',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='pindrop',
            name='pinvisiteddate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
