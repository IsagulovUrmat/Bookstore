# Generated by Django 3.1.6 on 2021-02-24 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0007_quotes_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotes',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Books.author'),
            preserve_default=False,
        ),
    ]
