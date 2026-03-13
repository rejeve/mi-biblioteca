from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import PublisherForm, AuthorForm, BookForm
from .models import Publisher, Author, Book

def home(request):
    return render(request, 'home2.html')

# ---------- Vistas Publisher ------------------
def add_publisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Editorial creada correctamente")
            return redirect('list_publisher')
    else:
        form = PublisherForm()
    return render(request, 'add_publisher.html', {'form':form})


def list_publisher(request):
    if request.method == 'GET':
        publishers = Publisher.objects.all()
        return render(request, 'list_publisher.html', {'publishers':publishers})
    
    
def edit_publisher(request, id):
    publisher = Publisher.objects.get(id=id)

    if request.method == 'POST':
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
            messages.success(request, "Editorial actualizada correctamente")
            return redirect('list_publisher')
    else:
        form = PublisherForm(instance=publisher)
    return render(request, 'edit_publisher.html', {'form':form, 'publisher': publisher})


def delete_publisher(request, id):
    publisher = Publisher.objects.get(id=id)

    if request.method == 'POST':
        publisher.delete()
        messages.warning(request, "La editorial se ha eliminado")
        return redirect('list_publisher')
    
    return render(request, 'delete_publisher.html', {'publisher':publisher})

# ----------------- Vistas Author -------------------------

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Autor creado correctamente")
            return redirect('list_authors')
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form':form})


def list_authors(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        return render(request, 'list_authors.html', {'authors':authors})
    

def edit_author(request, id):
    author = Author.objects.get(id=id)

    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            messages.success(request, "Autor actualizado correctamente")
            return redirect('list_authors')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'edit_author.html', {'form':form, 'author': author})


def delete_author(request, id):
    author = Author.objects.get(id=id)

    if request.method == 'POST':
        author.delete()
        messages.warning(request, "El autor se ha eliminado")
        return redirect('list_authors')
    
    return render(request, 'delete_author.html', {'author':author})


def author_detail(request, id):
    author = Author.objects.get(id=id)
    books = author.book_set.all()
    return render(request, 'author_detail.html', {'author':author,'books':books})

# ----------------- Vistas Book -------------------------
def list_book(request):
    if request.method == 'GET':
        books = Book.objects.all()
        return render(request, 'list_books.html', {'books':books})
    

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Libro creado correctamente")
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form':form})
    
def edit_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Libro actualizado correctamente")
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'book':book, 'form':form})

def delete_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.delete()
        messages.warning(request, "El libro se ha eliminado")
        return redirect('list_books')

    return render(request, 'delete_book.html', {'book':book})