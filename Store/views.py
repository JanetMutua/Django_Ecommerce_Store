from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.views.generic import ListView, DetailView



# Create your views here.

def Storefront(request):
    new = Product.objects.filter(new_arrival = 1)
    trending = Product.objects.filter(trending = 1)
    context = {'new': new, 'trending':trending}
    return render(request, 'Store/index.html', context)


# -----------------------------------------------shop view----------------------------------------

def Shop(request):
    products = Product.objects.filter(status=0)
    context = {'products': products}
    return render(request, 'Store/shop.html', context)

# ---------------------------------------------shop selections----------------------------------
def Trending(request):
    trending = Product.objects.filter(trending = 1)
    context = {'trending': trending}
    return render(request, 'Store/trending.html', context)

def Clearance(request):
    clearance = Product.objects.filter(clearance_sale = 1)
    context = {'clearance': clearance}
    return render(request, 'Store/clearance.html', context)


def NewArrival(request):
    new = Product.objects.filter(new_arrival = 1)
    context = {'new': new}
    return render(request, 'Store/newarrivals.html', context)


# ----------------------------------------------contact us---------------------------------------
def Contact(request):
    return render(request, 'Store/contact.html')
    
#-------------------------------------------------product views--------------------------------------- 

# def Product_detail(request, slug, pk):
#     if(Category.objects.filter(slug=slug, status=0)):
#         if(Product.objects.filter(pk = pk, status=0)):
#             products = Product.objects.filter(pk = pk, status=0).first()
#             context = {'products': products}
#         else:
#             messages.error(request, 'Something went wrong')
#             return redirect('categories')
        
#     else:
#         messages.error(request, 'Something went wrong')
#         return redirect('categories')
#     return render(request, 'Store/productdetail.html', context)

# categories views

# -----------------------------------------------------end of product views----------------------------------


def categories(request):
    category = Category.objects.filter(status=0)
    context = {'category': category}
    return render(request, 'Store/base.html', context)



def category_view(request, slug):
    if(Category.objects.filter(slug = slug, status=0)):
        products= Product.objects.filter(category__slug = slug)
        category_name = Category.objects.filter(slug = slug).first()
        context = {'products':products, 'category_name': category_name}
        return render(request, 'Store/base.html', context)

    else:
        messages.warning(request, 'No such Category')
        return redirect('/')



#---------------------------------------------------size views-----------------------------------------

def Shopsize(request):
    size = Size.objects.filter(status=0)
    context = {'size': size}
    return render(request, 'Store/shopsize.html', context)


def Sales(request):
    sale = Sale.objects.filter(status=0)
    context = {'sale': sale}
    return render(request, 'Store/sale.html', context)



# ----------------------------------------------cart and wishlist---------------------------------------

def Checkout(request):
    return render(request, 'Store/checkout.html')



def product_detail(request):
    return render(request, 'Store/productdetail.html')