# Generated by Django 4.1.2 on 2022-10-20 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AuthApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moderator',
            name='IsModerator',
        ),
    ]