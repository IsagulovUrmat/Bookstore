# Generated by Django 3.1.6 on 2021-02-18 14:14

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField(default=0, verbose_name='Возвраст')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('poster', models.ImageField(upload_to='books/', verbose_name='Постер')),
                ('year', models.PositiveIntegerField(default=2021, verbose_name='Дата выхода')),
                ('country', models.CharField(max_length=30, verbose_name='Страна')),
                ('publication_date', models.DateField(default=datetime.date.today, verbose_name='Дата публикации')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('authors', models.ManyToManyField(related_name='book_author', to='Books.Author', verbose_name='автор')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категория')),
                ('description', models.TextField(verbose_name='Описание')),
                ('ulr', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Категория')),
                ('description', models.TextField(verbose_name='Описание')),
                ('ulr', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Звезды рейтинга',
                'verbose_name_plural': 'Звезды рейтинга',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('text', models.TextField(max_length=5000, verbose_name='Сообщение')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Books.book', verbose_name='Книга')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Books.reviews', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP Адресс')),
                ('book', models.ForeignKey(on_delete=django.db.models.fields.CharField, to='Books.book', verbose_name='Книга')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Books.ratingstar', verbose_name='звезда')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.TextField(verbose_name='Цитата')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Books.book', verbose_name='Книга')),
            ],
            options={
                'verbose_name': 'Цитата из книги',
                'verbose_name_plural': 'Цитаты из книги',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Books.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(to='Books.Genre', verbose_name='жанры'),
        ),
    ]
