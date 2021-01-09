from django.shortcuts import render, HttpResponse

# Create your views here.

def homepage(request):
    return HttpResponse("Assalamu alaikum!")

def test(request):
    return render(request, "test.html")