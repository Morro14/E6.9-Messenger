# Generated by Django 4.1.7 on 2023-03-02 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='name',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
