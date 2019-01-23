import random

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView

# function based views
def home(request):
    num = random.randint(0,100000)
    some_list = [num, random.randint(0,100000), random.randint(0,100000)]
    context = {"bool_item": False, "num": num, "some_list": some_list}
    return render(request, 'home.html', context)

def contact(request):
    return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})

#class based views
class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        print(context)
        num = random.randint(0,100000)
        some_list = [num, random.randint(0,100000), random.randint(0,100000)]
        context = {"bool_item": True, "num": num, "some_list": some_list}
        return context

# class AboutView(TemplateView):
#     template_name = "about.html"
#
# class ContactView(TemplateView):
#     template_name = "contact.html"
