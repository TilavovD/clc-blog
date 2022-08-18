import datetime

from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from author.models import Author
from post.models import Post, Tag, Category
from post.serializer import PostSerializer
from author.serializer import AuthorDetailSerializer
from helpers.pagination import CustomPagination
from post.serializer import TagSerializer, CategorySerializer
"""
TODO:
    - AUTHOR DETAIL
    - AUTHOR DETAIL POST
"""


class TopAuthorListView(generics.ListAPIView):
    queryset = Author.objects.filter(is_top=True)
    serializer_class = AuthorDetailSerializer


class FeaturedPostsView(generics.ListAPIView):
    queryset = Post.objects.filter(is_featured=True)
    serializer_class = PostSerializer


class PopularPostsView(generics.ListAPIView):
    queryset = Post.objects.filter(is_popular=True)
    serializer_class = PostSerializer
    pagination_class = CustomPagination

class RecentlyPostsView(generics.ListAPIView):
    queryset = Post.objects.order_by("-published_date")
    serializer_class = PostSerializer

class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer()
