from django.db import models

# Create your models here.
class Categories(models.Model):
    categories = models.CharField(max_length=20, null=False, blank=False)
    date_created = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.categories


class Tags(models.Model):
    tag = models.CharField(max_length=200, null=False, blank=False)
    date_created = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.tag

class Blog(models.Model):
    author = models.CharField(max_length=100, blank=False, null=False)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE )
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE )
    post = models.TextField(max_length=1000)
    date_created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.author
    
