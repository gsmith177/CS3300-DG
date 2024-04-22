# Generated by Django 4.2 on 2024-04-06 21:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('email', models.CharField(max_length=200)),
                ('is_active', models.BooleanField()),
                ('skill_level', models.CharField(choices=[('Professional', 'Average score under par'), ('Intermediate', 'Average score on par'), ('Beginner', 'Average score over par')], max_length=200)),
                ('date_joined', models.DateField(default=datetime.date.today, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('location', models.CharField(max_length=200)),
                ('num_joined', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.user')),
            ],
        ),
    ]