# Generated by Django 5.1.1 on 2024-10-20 12:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=255, verbose_name='место, в котором выполняется привычка')),
                ('time', models.TimeField(verbose_name='время, в которое выполняется привычка')),
                ('action', models.CharField(max_length=255, verbose_name='действие, которое представляет собой привычка')),
                ('is_pleasant', models.BooleanField(default=False, verbose_name='полезность привычки')),
                ('periodicity', models.IntegerField(default=1, verbose_name='переодичность')),
                ('reward', models.CharField(blank=True, max_length=255, null=True, verbose_name='вознаграждение')),
                ('time_to_complete', models.DurationField(default='00:01:00', verbose_name='время на выполнение')),
                ('is_public', models.BooleanField(default=False, verbose_name='признак публичности')),
                ('linked_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='linked_to', to='habits.habit', verbose_name='связанность привычки')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
            },
        ),
    ]
