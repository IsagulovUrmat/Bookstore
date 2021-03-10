from django import template
from Books.models import Category, Book

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('Books/tags/last_book.html')
def get_last_books():
    books = Book.objects.order_by("-id")[:5]
    return {"last_books": books}
