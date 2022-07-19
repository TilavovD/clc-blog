from django.contrib import admin
from django.urls import path, include
from author.views import AuthorDetailView,AuthorPostsView
urlpatterns = [
    path('author/<int:id>/', AuthorDetailView.as_view()),
    path('author/<int:author_id>/posts/', AuthorPostsView.as_view()),
]
