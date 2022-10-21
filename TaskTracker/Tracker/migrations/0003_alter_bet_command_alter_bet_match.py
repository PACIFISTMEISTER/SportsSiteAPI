# Generated by Django 4.1.2 on 2022-10-16 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0002_alter_command_options_alter_match_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='Command',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Command', to='Tracker.command'),
        ),
        migrations.AlterField(
            model_name='bet',
            name='Match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Match', to='Tracker.match'),
        ),
    ]