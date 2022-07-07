from multiprocessing import context
import re
from django.shortcuts import render, redirect
from django.contrib import messages
from Store.models import *
from Store.forms import CustomUserForm
from django.contrib.auth import authenticate, login, logout
# from Cart.models import Order



def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        name = request.POST.get('username')
        passwd1 = request.POST.get('password1')
       
        form = authenticate(request, username = name, password = passwd1)
         
        if form.is_valid():
            form.save()
            messages.success(request, 'Signup was successful.Login to shop')
            return redirect('/login')


    context= {'form': form}
    return render(request, 'Store/auth/register2.html', context)


def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in')
        return redirect('/')
    else:

        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request, username = name, password = passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in Successfully')
                return redirect('/')
            else:
                messages.error(request, 'Invalid Username or Password')
                return redirect('/login')

        return render(request, 'Store/auth/login2.html')

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Logged out Successfully')
        return redirect('/')
    return redirect('/')



# -------------------------------profile view---------------------

# def my_profile(request):
#     my_user_profile = Profile.objects.filter(user = request.user).first()
#     my_orders = Order.objects.filter(is_ordered = True, owner=my_user_profile)
#     context = {
#         'my_orders': my_orders
#     }
#     return render(request, 'Store/profile.html', context)