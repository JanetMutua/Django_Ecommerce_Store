from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from Store.models import Product, Cart




# @login_required(login_url='loginpage')


def index_cart(request):
    cart = Cart.objects.filter(user = request.user)
    context = {'cart': cart}
    return render(request, 'Store/cart.html', context)

def myCart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if(product_check):
                if(Cart.objects.filter(user=request.user.id, product_id = prod_id)):
                    return JsonResponse({'status': "Already In Cart"})
                else:
                    prod_qty = int(request.POST.get('product_qty'))
                    if product_check.quantity >= prod_qty:
                        Cart.objects.create(user = request.user, product_id  = prod_id, product_qty = prod_qty)
                        return JsonResponse({'status': "Product added successfully"})
                    else:
                        return JsonResponse({'status': "Only "+ str(product_check.quantity)+ "available"})
            else:
                return JsonResponse({'status': "Something went wrong"})

        else:
            return JsonResponse({'status': "Login to Continue"})
    return redirect('/')


