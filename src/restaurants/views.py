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
    return render(request, 'base.html', {"str_var": True})
