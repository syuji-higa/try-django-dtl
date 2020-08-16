from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def index(request):
    return HttpResponse('Hello World!')

def book_list(request):
    # books = Book.objects.all()
    books = Book.objects.filter(publisher='翔泳社')
    return render(request, 'main/book_list.html', {
        'books': books
    })

def rel(request):
    return render(request, 'main/rel.html', {
        'book': Book.objects.get(pk=1)
    })
