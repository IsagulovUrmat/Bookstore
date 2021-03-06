# Generated by Django 3.1.6 on 2021-03-03 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0012_auto_20210301_2022'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ratingstar',
            options={'ordering': ['-value'], 'verbose_name': 'Звезды рейтинга', 'verbose_name_plural': 'Звезды рейтинга'},
        ),
        migrations.AlterField(
            model_name='book',
            name='url',
            field=models.CharField(max_length=160, unique=True),
        ),
    ]
