from django.shortcuts import render
from .models import Categorias, Posts


def index(request):
    posts = Posts.objects.all() 
    return render(request, 'index.html', {'Posts': posts})  

