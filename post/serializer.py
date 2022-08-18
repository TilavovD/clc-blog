from rest_framework import serializers
from post.models import Post, Tag, Category


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"