# Generated by Django 4.1.2 on 2022-10-16 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Winrate', models.PositiveSmallIntegerField()),
                ('Symbol', models.ImageField(upload_to='static/images')),
                ('CurrentOpponent', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Tracker.command')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Surname', models.CharField(max_length=100)),
                ('Earingngs', models.PositiveIntegerField(default=0)),
                ('MatchesPlayed', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.PositiveIntegerField()),
                ('BetForOne', models.PositiveIntegerField()),
                ('BetForTwo', models.PositiveIntegerField()),
                ('Date', models.DateTimeField()),
                ('CommandOne', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='CommandOne', to='Tracker.command')),
                ('CommandTwo', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='CommandTwo', to='Tracker.command')),
                ('Winner', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Winner', to='Tracker.command')),
            ],
        ),
        migrations.AddField(
            model_name='command',
            name='Players',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Players', to='Tracker.player'),
        ),
    ]
