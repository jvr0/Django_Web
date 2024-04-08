from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    image = models.ImageField(upload_to="books")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated = models.DateTimeField(auto_now=True, verbose_name= "Updated Date")
    
    def __str__(self):
        return self.title

class Film(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    image = models.ImageField(upload_to="films")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated = models.DateTimeField(auto_now=True, verbose_name= "Updated Date")
    
    def __str__(self):
        return self.title
    
class Show(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    image = models.ImageField(upload_to="shows")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated = models.DateTimeField(auto_now=True, verbose_name= "Updated Date")

    def __str__(self):
        return self.title

class Music(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    image = models.ImageField(upload_to="musics")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated = models.DateTimeField(auto_now=True, verbose_name= "Updated Date")

    def __str__(self):
        return self.title