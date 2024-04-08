from django.contrib import admin
from .models import *

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')

admin.site.register(Book, BookAdmin)

class FilmAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')

admin.site.register(Film, FilmAdmin)

class ShowAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')

admin.site.register(Show, ShowAdmin)

class MusicAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')

admin.site.register(Music, MusicAdmin)