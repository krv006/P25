from django.shortcuts import render

from apps.models import Friend, Account, Product, Category


def profil_page(request):
    context = {
        'friends': Friend.objects.all(),
        'accounts': Account.objects.all()
    }
    return render(request, 'apps/task1/profil.html', context)



def index(request):
    context = {
        'categories': Category.objects.all(),
    }
    return render(request, 'apps/task2/index.html', context)


def product_page(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'apps/task2/product.html', context)
