# Generated by Django 4.2 on 2024-04-22 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0006_user_groups_user_is_superuser_user_last_login_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
