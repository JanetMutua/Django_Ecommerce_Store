from multiprocessing import context
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from Store.models import Product, Cart, Wishlist


@login_required(login_url='loginpage')
def index(request):
    wishlist = Wishlist.objects.filter(user = request.user)
    context = {'wishlist': wishlist}
    return render(request, 'Store/wishlist.html', context)

# ajax call
def addToWishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)

            if(product_check):
                if(Wishlist.objects.filter(user=request.user, product_id=prod_id)):
                    return JsonResponse({'status':"Already added to Wishlist"})
                else:
                    Wishlist.objects.create(user=request.user, product_id = prod_id)
                    return JsonResponse({'status':"Added to wishlist"})
            else:
                return JsonResponse({'status':"Product Not available"})
        else:
            return JsonResponse({'status':"Login to continue"})
    return redirect('/')


def deletewishlistitem(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))

            if(Wishlist.objects.filter(user=request.user, product_id=prod_id)):
                wishlistitem = Wishlist.objects.get(product_id=prod_id)
                wishlistitem.delete()
                return JsonResponse({'status':"Removed from Wishlist"})
            else:
                Wishlist.objects.create(user=request.user, product_id = prod_id)
                return JsonResponse({'status':"Something went wrong"})
        else:
            return JsonResponse({'status':"Login to continue"})
    return redirect('/')
        