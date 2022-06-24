from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView


# Create your views here.

# class Home(ListView):
#      context_object_name = 'item'
#      queryset = Product.objects.filter(status= 0)
#      template_name = 'Store/index.html'

def Storefront(request):
    new = Product.objects.filter(new_arrival = 1)
    trending = Product.objects.filter(trending = 1)
    context = {'new': new, 'trending':trending}
    return render(request, 'Store/index.html', context)




# -----------------------------------------------shop view----------------------------------------

class Shop(ListView):
     context_object_name = 'products'
     queryset = Product.objects.filter(status=0)
     template_name = 'Store/shop.html'



# ---------------------------------------------shop selections----------------------------------

class Trending(ListView):
     context_object_name = 'trending'
     queryset = Product.objects.filter(trending= 1)
     template_name = 'Store/trending.html'


class Clearance(TemplateView):
    template_name = 'Store/clearance.html'


    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        clearance_sale = Product.objects.filter(clearance_sale= 1)
        plussize = Category.objects.filter(PlusSize = 1)
        clearance = Category.objects.filter(Clearance= 1)
        petite = Category.objects.filter(Petite = 1)

        context =  super(Clearance, self).get_context_data(*args, **kwargs)
        context = {'cat_menu': cat_menu, 'clearance_sale': clearance_sale, 'plussize':plussize, 'petite':petite, 'clearance': clearance}  
            
        return context


class NewArrival(TemplateView):
    model = Product
    template_name = 'Store/newarrivals.html'
    paginate_by = 2


    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        new = Product.objects.filter(new_arrival = 1)
        plussize = Category.objects.filter(PlusSize = 1)
        clearance = Category.objects.filter(Clearance= 1)
        petite = Category.objects.filter(Petite = 1)

        context =  super(NewArrival, self).get_context_data(*args, **kwargs)
        context = {'cat_menu': cat_menu, 'new': new, 'plussize':plussize, 'petite':petite, 'clearance': clearance}  
            
        return context

    


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
    return render(request, 'Store/categories.html', context)



def category_view(request, slug):
    if(Category.objects.filter(slug = slug, status=0)):
        products= Product.objects.filter(category__slug = slug)
        category_name = Category.objects.filter(slug = slug).first()
        context = {'products':products, 'category_name': category_name}
        return render(request, 'Store/product_category.html', context)

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