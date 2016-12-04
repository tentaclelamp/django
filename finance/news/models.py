from django.db import models
from django.contrib import admin

# Create your models here.

class Blogspost(models.Model):
        title = models.CharField(max_length=150)
        body=models.TextField()
        timestamp=models.DateTimeField()
        def __init__(self, tittle):
                super(Blogspost, self).__init__()
                self.Tittle = tittle
admin.site.register(Blogspost)
