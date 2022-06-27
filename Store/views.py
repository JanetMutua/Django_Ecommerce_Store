from pyexpat import model
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


class NewArrival(ListView):
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

class ProductDetailView(DetailView):
    model = Product
    template = 'Store/product_detail.html'


    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        new = Product.objects.filter(new_arrival = 1)
        plussize = Category.objects.filter(PlusSize = 1)
        clearance = Category.objects.filter(Clearance= 1)
        petite = Category.objects.filter(Petite = 1)
        products = Product.objects.filter(slug__icontains=self.kwargs.get('slug'))

        context =  super(ProductDetailView, self).get_context_data(**kwargs)
        context = {'products':products, 'cat_menu': cat_menu, 'new': new, 'plussize':plussize, 'petite':petite, 'clearance': clearance}  
            
        return context

# -----------------------------------------------------end of product views----------------------------------


class CategoryTemplateView(ListView):
    model = Product
    template_name = 'Store/product_category.html'
        

    def get_context_data(self, **kwargs):
        products = Product.objects.filter(category__slug__icontains = self.kwargs.get('slug'))
        category_name = Category.objects.filter(slug__icontains=self.kwargs.get('slug'))

        cat_menu = Category.objects.all()
        new = Product.objects.filter(new_arrival = 1)
        plussize = Category.objects.filter(PlusSize = 1)
        clearance = Category.objects.filter(Clearance= 1)
        petite = Category.objects.filter(Petite = 1)

        context =  super(CategoryTemplateView, self).get_context_data(**kwargs)
        context = {'products': products, 'category_name':category_name, 'cat_menu': cat_menu, 'new': new, 'plussize':plussize, 'petite':petite, 'clearance': clearance}
        return context
    


#---------------------------------------------------size views-----------------------------------------

def Shopsize(request):
    size = Size.objects.filter(status=0)
    context = {'size': size}
    return render(request, 'Store/shopsize.html', context)



def categories(request):
    category = Category.objects.filter(status=0)
    context = {'category': category}
    return render(request, 'Store/categories.html', context)





def Sales(request):
    sale = Sale.objects.filter(status=0)
    context = {'sale': sale}
    return render(request, 'Store/sale.html', context)



# ----------------------------------------------cart and wishlist---------------------------------------

def Checkout(request):
    return render(request, 'Store/checkout.html')


