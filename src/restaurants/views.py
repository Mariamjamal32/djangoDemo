from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# functions based views
def home(request):
    return HttpResponse("Hello django!")
