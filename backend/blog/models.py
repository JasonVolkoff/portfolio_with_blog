from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify
# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=50)

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    category = models.CharField(max_length=50)
    thumbname = models.ImageField(upload_to='photos/%Y/%m/%d')
    excerpt = models.CharField(max_length=200)
    month = models.CharField(max_length=3)
    day = models.CharField(max_length=2)
    content = models.TextField()
    featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title 

        