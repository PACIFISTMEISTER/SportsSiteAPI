# Generated by Django 4.1.2 on 2022-10-16 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0006_auto_20221016_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='IsClosed',
            field=models.BooleanField(default=False),
        ),
    ]
