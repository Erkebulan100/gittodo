from django.shortcuts import render, HttpResponse
from .models import ToDo, Book

# Create your views here.

def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

    

def test2(request):
    
    book_store = Book.objects.all()
    return render(request, "books.html", {"book_store": book_store})

    # return HttpResponse("This is the second test page")

def third(request):
    return HttpResponse("This is page test3")