from django.shortcuts import render,redirect

# Create your views here.
def index(requests):
    render(request,'index.html')

def intro(requests):
    render(request,'intro.html')

def blog(requests):
    render(request,'blog.html')

def contact(requests):
    render(request,'contact.html')

def services(requests):
    render(request,'services.html')