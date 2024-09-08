from django.contrib import admin
from .models import Author, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_per_page = 4
    search_fields = ['title', 'author']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Informations du Manga", {'fields' : ['title', 'author']}),
        ("Informations Magasin", {'fields': ['quantity']}),
    ]
    list_display = ('title', 'author', 'quantity')
    list_filter = ['author']
    search_fields = ['title', 'author__name']
    list_per_page = 4