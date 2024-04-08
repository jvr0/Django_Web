from django.db import models

# Create your models here.

class Blog (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="Blogs")
    url = models.URLField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated = models.DateTimeField(auto_now=True, verbose_name= "Updated Date")
    
    class Meta:
        ordering = ["created"] #Fecha de creación inversa, para hacer la otra ["-created"]
        
    def __str__(self):
        return self.title