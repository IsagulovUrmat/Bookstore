# Generated by Django 3.1.6 on 2021-02-18 14:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0002_auto_20210218_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='age',
        ),
        migrations.AddField(
            model_name='author',
            name='birthdate',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата рождения'),
        ),
        migrations.AddField(
            model_name='author',
            name='date_of_death',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата смерти'),
        ),
    ]
