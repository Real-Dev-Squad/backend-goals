# Generated by Django 4.0.9 on 2023-05-10 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, default='', max_length=200)),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='date published')),
                ('created_by', models.CharField(blank=True, max_length=50)),
                ('user_id', models.CharField(max_length=50)),
                ('starts_on', models.DateTimeField(null=True)),
                ('ends_on', models.DateTimeField(null=True)),
                ('percentage_completed', models.IntegerField(default=0)),
                ('assigned_by', models.CharField(blank=True, max_length=200)),
                ('status', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
