from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Book, Author
from .forms import BookForm

def index(request):
    context = {"books": Book.objects.all()}
    return render(request, "mangalib/index.html", context)

def show(request, book_id):
    context = {"book" : get_object_or_404(Book, pk = book_id)}
    return render(request, 'mangalib/show.html', context)

def add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
    
        if form.is_valid():
            form.save()
            return redirect("mangalib:index")
    else:
        form = BookForm()

    return render(request, 'mangalib/book-form.html', {"form": form})

def edit(request, book_id):
    book = Book.objects.get(pk = book_id)

    if request.method == "POST":
        form = BookForm(request.POST, instance = book)
    
        if form.is_valid():
            form.save()
            return redirect("mangalib:index")
    else:
        form = BookForm()

    return render(request, 'mangalib/book-form.html', {"form": form})

def remove(request, book_id): 
    book = Book.objects.get(pk = book_id)
    book.delete()
    return redirect('mangalib:index')