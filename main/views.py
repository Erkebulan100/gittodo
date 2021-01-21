from django.shortcuts import render, HttpResponse, redirect
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

def test3(request):

    book_store = Book.objects.all()
    return render(request, "book_details.html", {"book_store": book_store})

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    print(text)
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)
def add_book(request):
    form = request.POST
    name = form["book_name"]
    title = form["book_title"]
    subtitle = form["book_subtitle"]
    description = form["book_description"]
    genre = form["book_genre"]
    author = form["book_author"]
    year = form["book_year"]
    price = form["book_price"]
    book = Book(name=name, title=title, subtitle=subtitle, description=description, genre=genre, author=author, year=year, price = price)
    book.save()
    return redirect(test2)


def delete_todo(request, id): 
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)

def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)

def delete_book(request, id): 
    book = Book.objects.get(id=id)
    book.delete()
    return redirect(test2)

def mark_book(request, id):
    book = Book.objects.get(id=id)
    book.is_favorite = True
    book.save()
    return redirect(test2)

def unmark_book(request, id):
    book = Book.objects.get(id=id)
    book.is_favorite = False
    book.save()
    return redirect(test2)

def BooksDetail(request, id):
    book = Book.objects.get(id=id)
    book.save()
    return redirect(test3)

