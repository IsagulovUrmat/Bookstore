

from django.db import models
from datetime import date

from django.urls import reverse


class Category(models.Model):
    name = models.CharField("Категория",max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"



class Author(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField("Описание")
    birthdate = models.DateField("Дата рождения", default=date.today)
    date_of_death = models.DateField("Дата смерти", default=date.today)
    image = models.ImageField("Изображение", upload_to="authors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Genre(models.Model):
    name = models.CharField("Категория", max_length=100)
    description = models.TextField("Описание")
    ulr = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

class Book(models.Model):
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    poster = models.ImageField("Обложка", upload_to="books/")
    year = models.PositiveIntegerField("Год издания", default=2021)
    country = models.CharField("Страна", max_length=30)
    authors = models.ManyToManyField(Author, verbose_name="автор", related_name="book_author")
    genres = models.ManyToManyField(Genre, verbose_name="жанры")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    url = models.CharField(max_length=160, unique=True)
    draft = models.BooleanField("Черновик", default=False)
    price = models.PositiveIntegerField("Цена", default=100)
    bookfile = models.FileField(verbose_name="Файл книги")
    average = models.FloatField(default=1.0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.url })

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

class Quotes(models.Model):
    title = models.CharField(max_length=100)
    quote = models.TextField("Цитата")
    book = models.ForeignKey(Book, verbose_name="Книга", on_delete=models.CASCADE)
    author = models.ForeignKey(Author, verbose_name="Автор", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Цитата из книги"
        verbose_name_plural = "Цитаты из книги"


class RatingStar(models.Model):
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезды рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]


class Rating(models.Model):
    ip = models.CharField("IP Адресс", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Книга")

    def __str__(self):
        return f"{self.star} - {self.book}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    book = models.ForeignKey(Book, verbose_name="Книга", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.book}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"








