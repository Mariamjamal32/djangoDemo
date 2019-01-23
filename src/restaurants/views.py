import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# functions based views
# def home(request):
    # str_var= "rendered"
    # html_= f"""
    #     <!DOCTYPE html>
    #     <html lang=en>
    #         <head>
    #         </head>
    #         <body>
    #             <h1> HTML View </h1>
    #             <p> This is {str_var} HTML. </p>
    #         </body>
    #     <html>
    # """
    # return HttpResponse(html_)

def home(request):
    num = random.randint(0,100000)
    some_list = [num, random.randint(0,100000), random.randint(0,100000)]
    return render(request, 'home.html', {"bool_item": False, "num": num, "some_list": some_list})

def contact(request):
    return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})
