# Generated by Django 4.1.2 on 2022-10-17 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0009_rename_isclosed_match_isactive'),
    ]

    operations = [
        migrations.RenameField(
            model_name='command',
            old_name='Winrate',
            new_name='Wins',
        ),
    ]
