# Generated by Django 4.1.2 on 2022-10-17 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0008_remove_match_betforone_remove_match_betfortwo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='IsClosed',
            new_name='IsActive',
        ),
    ]
