from django.db import models
from datetime import datetime
from django.db.models.deletion import PROTECT
from django.template.defaultfilters import slugify
# Create your models here.


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
    
    def save(self, *args, **kwargs):
        """
        Custom save method automatically assigns slug to be the blog's title. It 
        also allows BlogPosts to share the same slug name while being unique from 
        one another by appending an integer to similar BlogPosts.

        """
        original_slug = slugify(self.title)
        queryset = BlogPost.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        while(queryset): 
            slug = original_slug + '-' + str(count)
            count +=1
            queryset = BlogPost.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug
        """
        Upon saving a BlogPost, the "featured" boolean determines if that post is
        to be Featured on the front page. If True, the logic below identifies
        the previous featured post and sets it to False
        """
        if self.featured:
            try:
                temp = BlogPost.objects.get(featured=True)
                if self != temp:
                    temp.featured = False
                    temp.save

            except BlogPost.DoesNotExist:
                pass
            
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)
    post = models.ForeignKey(BlogPost, on_delete=PROTECT, related_name='categories')

    def __str__(self):
        return self.title

        