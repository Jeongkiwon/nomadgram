# Generated by Django 2.0.8 on 2018-11-07 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_notifications_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notifications',
            old_name='images',
            new_name='image',
        ),
    ]
