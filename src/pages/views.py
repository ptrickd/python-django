from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs):
    print(request.user)
    # return HttpResponse('<h1>Hello World</h1')
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about me",
        "my_number": 123,
        "my_list": [1, 2, 3]
    }
    return render(request, "about.html", my_context)
