# Generated by Django 4.1.2 on 2022-10-16 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0007_match_isclosed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='BetForOne',
        ),
        migrations.RemoveField(
            model_name='match',
            name='BetForTwo',
        ),
    ]
