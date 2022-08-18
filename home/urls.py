from django.contrib import admin
from django.urls import path, include
from .views import PopularPostsView, FeaturedPostsView, TopAuthorListView, RecentlyPostsView, CategoryListView, TagListView
urlpatterns = [
    path('top_author/', TopAuthorListView.as_view()),
    path('featured_posts/', FeaturedPostsView.as_view()),
    path('popular_posts/', PopularPostsView.as_view()),
    path('category/', CategoryListView.as_view()),
    path('tag/', TagListView.as_view()),
    path("recently_posts", RecentlyPostsView.as_view())
]
