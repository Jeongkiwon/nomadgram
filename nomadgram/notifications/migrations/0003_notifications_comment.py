# Generated by Django 2.0.8 on 2018-11-06 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_auto_20181105_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
