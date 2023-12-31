from django.db import models
from django.template.defaultfilters import slugify

class WebsiteSetting (models.Model):
    title = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logo')
    email = models.EmailField()
    mobile = models.CharField(max_length=12)
    address = models.TextField()

    def __str__(self):
        return self.title



class Slider(models.Model):
    heading = models.CharField(max_length=55)
    sub_heading = models.CharField(max_length=35)
    image = models.ImageField(upload_to='slider')
    status = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.heading} {self.sub_heading}"
    


class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,null=True, blank=True)
    description = models.TextField()
    author = models.CharField(max_length=255)
    date_time = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blog')
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        """overriding"""
        self.slug= slugify(self.title) 
        super(Blog, self).save(*args, **kwargs)



class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name='FAQ'
        verbose_name_plural= 'List of FAQ'