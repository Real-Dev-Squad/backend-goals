# Generated by Django 4.0.9 on 2023-09-12 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='roles',
            field=models.JSONField(default={}),
        ),
    ]
