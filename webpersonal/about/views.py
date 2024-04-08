from django.shortcuts import render
from .models import *

# Create your views here.

def about(request):
    books = Book.objects.all()
    films = Film.objects.all()
    shows = Show.objects.all()
    musics = Music.objects.all()
    return render(request, "about/about.html", {'books': books, 'films': films, 'shows': shows, 'musics': musics})