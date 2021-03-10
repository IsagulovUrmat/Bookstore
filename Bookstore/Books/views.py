from django.db.models import Q, Avg
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .forms import ReviewForm, RatingForm
from .models import *

# <button class="btn1 btn" >Купить</button>

class GenreYear:

    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Book.objects.filter(draft=False).values("year")


class BooksView(GenreYear, ListView):
    model = Book
    queryset = Book.objects.filter(draft=False)
    template_name =  "Books/books.html"
    paginate_by = 9




class BookDetailView(GenreYear, DetailView):
    model = Book
    slug_field = "url"
    template_name = "Books/book_details.html"
    # extra_context = {'average': Book.average.all()}

    # def get_context_data(self, *args, **kwargs):
    #     context = super(Book,self).get_context_data(*args, **kwargs)
    #     total = 0
    #     for i in Book.average:
    #         total += i.rate
    #     # add extra field
    #     context["average"] = total / len(Book.average)
    #     return context

    # def get_average(self, book_id, **kwargs):
    #     book = Book.objects.get(id=book_id)
    #     context = super(Book, self).get_context_data(**kwargs)
    #     context['comments'] = self.object.comment_set.filter(approved=True)
    #     total = 0
    #     for i in rates:
    #         total += i.rate
    #     context = {'book': total / len(rates)}
    #     return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["average"] = (Book.objects.all().annotate(avg_review=Avg('rates__average')))
    #     return context


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["star_form"] = RatingForm()
        return context


def book_detail(request,book_id):

    try:
        book = Book.objects.get(id=book_id)
        fil1 = book.bookfile.open()
        return HttpResponse(fil1.read()[:200000])
    except FileNotFoundError:
        return HttpResponse("Вы не можете прочитать эту книгу!")




def QuoteViews(request, pk):
    book = Book.objects.get(id=pk)
    quote = Quotes.objects.filter(book_id=book.id)
    return render(request, "Books/quotes.html", {"quote": quote},)

class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        book = Book.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.book = book
            form.save()
        return redirect(book.get_absolute_url())


def Author_view(request,author_name):
    author = Author.objects.get(name=author_name)
    return render(request, "Books/author.html", {"author":author})

class FilterBooksView(GenreYear, ListView):
    template_name = "Books/books.html"
    paginate_by = 9

    def get_queryset(self):
        queryset = Book.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist("genre"))
        ).distinct()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["year"] = ''.join([f"year={x}&" for x in self.request.GET.getlist("year")])
        context["genre"] = ''.join([f"genre={x}&" for x in self.request.GET.getlist("genre")])
        return context

class AddStarRating(View):
    """Добавление рейтинга фильму"""
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                book_id=int(request.POST.get("book")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)

class Search(GenreYear,ListView):
    template_name = "Books/books.html"
    paginate_by = 9
    def get_queryset(self):
        return Book.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context






