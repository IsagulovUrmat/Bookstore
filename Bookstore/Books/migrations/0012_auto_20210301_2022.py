# Generated by Django 3.1.6 on 2021-03-01 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0011_book_bookfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookfile',
            field=models.FileField(upload_to='', verbose_name='Файл книги'),
        ),
    ]