# Generated by Django 4.1.7 on 2023-03-31 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_myuser_profile picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='profile picture',
            new_name='file_field',
        ),
    ]