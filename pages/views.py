from django.http import request
from django.shortcuts import render
from  .models import ContactModel


# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'base.html')

def contact(request):
    form = ContactModel.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        else:
            print('Uzur')

    else:
        print(form)
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def shop(request):
    return render(request, 'shop.html')   

def elements(request):
    return render(request, 'elements.html')

def portfolio_item(request):
    return render(request, 'portfolio-item.html')


def blog_single(request):
    return render(request, 'blog-single.html')


def shop_single(request):
    return render(request, 'shop-single.html')


def portfolio_category(request):
    return render(request, 'portfolio-category.html')