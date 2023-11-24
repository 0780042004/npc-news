from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def global_news(request):
    return render(request,'global_news.html')

def undergraduates(request):
    return render (request,'undergraduates.html')