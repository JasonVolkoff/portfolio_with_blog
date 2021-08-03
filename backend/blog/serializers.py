from rest_framework import serializer
from .models import BlogPost, Category

class BlogPostSerializer(serializer.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
        lookup_field = 'slug'

class CategorySerializer(serializer.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        lookup_field = 'name'