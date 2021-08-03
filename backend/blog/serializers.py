from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializer.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
        lookup_field = 'slug'