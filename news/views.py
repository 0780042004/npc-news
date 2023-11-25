from django.http import HttpResponse
from django.shortcuts import render
from .models import post

# Create your views here.
def home(request):
    posts = post.objects.all()
    return render(request,'home.html', {'posts': posts})

def global_news(request):
    return render(request,'global_news.html')

def undergraduates(request):
    return render (request,'undergraduates.html')
