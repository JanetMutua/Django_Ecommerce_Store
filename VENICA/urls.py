"""VENICA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Store.views import *
from django.conf import settings
from django.conf.urls.static import static
from Store.controller import authview, cart, wishlist


urlpatterns = [

    #-------------------------------------------------test product detail view-------------------------------

    # path('products/<int:pk>/', ProductDetailView.as_view(), name='productdetail'),



    #----------------------------------------------other urls----------------------------------------

    path('admin/', admin.site.urls),
    path('', Storefront, name='home'),
    path('contact-us/', Contact, name = 'contact'),
    

    # ------------------------------------------shop urls-----------------------------------------------------

    path('shopsize/', Shopsize, name='shopsize'),
    path('Shop/', Shop, name='shop'),



    # -----------------------------------------add to wishlist-----------------------------------------------

    path('wishlist', wishlist.index, name='wishlist'),

    # -----------------=--------------------ajax-------------------------
    path('add-to-wishlist', wishlist.addToWishlist, name='addtowishlist'),
    path('delete-wishlist-item', wishlist.deletewishlistitem, name='deletewishlistitem'),

    # ----------------------------------------------------end wishlist---------------------------------------

    # ------------------------------------------------------add to cart--------------------------------------

    path('mycart', cart.index_cart, name='mycart'),
    path('add-to-cart', cart.myCart, name='addtocart'),
    path('checkout', Checkout, name='checkout'),
  

    #------------------------------registration and login urls-------------------------------------------

    path('register/', authview.register, name='register'),
    path('login/', authview.loginpage, name='loginpage'),
    path('logout/', authview.logoutpage, name='logout'),
    
    #------------------------------------------fetching products------------------------------------------

    path('category', categories, name='category'),


    path('categories/<str:slug>', category_view, name='product_category'),

    # path('categories/<str:slug>/<int:pk>', Product_detail, name='productdetail'),

    path('trending/', Trending, name='trending' ),
    path('clearancesales/', Clearance, name='clearance'),
    path('newarrivals/', NewArrival, name='newarrival'),







    
    #----------------------------------------passwords reset links----------------------------------------------


    # path('password_reset/', auth_views.PasswordResetView.as_view(
    #     template_name='users/password_reset.html'), name='password_reset'),

    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
    #     template_name='users/password_reset_done.html'), name='password_reset_done'),

    #path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),

    # --------------------------------------------------end of password reser links---------------------------------------

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)