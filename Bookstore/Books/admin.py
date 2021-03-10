from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "url"]
    list_display_links = ["name",]

class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ["name", "email"]

class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "url", "draft", "get_poster"]
    list_filter = ["category", "year"]
    search_fields = ["title", "category__name"]
    inlines = [ReviewInline]
    save_on_top = True
    list_editable = ["draft",]

    def get_poster(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="50" height="60"')

    get_poster.short_description = "Изображение"

class ReviewAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "parent", "book", "id"]
    readonly_fields = ["name", "email"]

class GenreAdmin(admin.ModelAdmin):
    list_display = ["name",]

class QuotesAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "book"]

class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", "get_image"]
    readonly_fields = ["get_image",]

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"


class RatingAdmin(admin.ModelAdmin):
    list_display = ["star", "book", "ip",]


# admin.site.register(Category)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Quotes, QuotesAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(RatingStar)
admin.site.register(Reviews, ReviewAdmin)
