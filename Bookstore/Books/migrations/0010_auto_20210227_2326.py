# Generated by Django 3.1.6 on 2021-02-27 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0009_auto_20210224_2100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='ulr',
            new_name='url',
        ),
    ]