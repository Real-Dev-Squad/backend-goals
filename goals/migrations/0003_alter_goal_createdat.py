# Generated by Django 4.0.9 on 2023-04-28 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0002_alter_usergoal_endson_alter_usergoal_startson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='createdAt',
            field=models.DateTimeField(auto_now=True, verbose_name='date published'),
        ),
    ]
