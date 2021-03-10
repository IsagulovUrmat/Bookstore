from django.urls import path
from . import views

urlpatterns = [
    path("", views.BooksView.as_view()),
    path("filter/", views.FilterBooksView.as_view(), name="filter"),
    path("search/", views.Search.as_view(), name="search"),
    path("add-rating/", views.AddStarRating.as_view(), name='add_rating'),
    path("<slug:slug>/", views.BookDetailView.as_view(), name='book_detail'),
    path("author/<str:author_name>/", views.Author_view, name='author_detail'),
    path("review/<int:pk>/", views.AddReview.as_view(), name='add_review'),
    path("quotes/<int:pk>/", views.QuoteViews, name='quotes'),
    path("file/<int:book_id>/", views.book_detail, name="file"),
]