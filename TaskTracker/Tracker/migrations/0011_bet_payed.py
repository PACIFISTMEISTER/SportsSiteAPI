# Generated by Django 4.1.2 on 2022-10-17 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0010_rename_winrate_command_wins'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='Payed',
            field=models.BooleanField(default=False),
        ),
    ]