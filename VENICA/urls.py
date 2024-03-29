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
from Store.controller import authview, cart, wishlist, quicklinks


urlpatterns = [

    #-------------------------------------------------test product detail view-------------------------------

    # path('products/<int:pk>/', ProductDetailView.as_view(), name='productdetail'),



    #----------------------------------------------other urls----------------------------------------

    path('admin/', admin.site.urls),
    path('', Homeview.as_view(), name='home'),
    path('contact-us/', ContactView.as_view(), name = 'contact'),
    

    # ------------------------------------------shop urls-----------------------------------------------------

    path('shopsize/', Shopsize, name='shopsize'),
    path('Shop/', Shop.as_view(), name='shop'),
    path('sales/', Sales, name="sales"),


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

    # path('category', categories, name='category'),


    path('categories/<str:slug>', CategoryTemplateView.as_view(), name='product_category'),
    path('plussize/<str:slug>', PlusTemplateView.as_view(), name='plussize'),
    path('petite/<str:slug>', PetiteTemplateView.as_view(), name='petite'),

    path('shop/<str:slug>', ProductDetailView.as_view(), name='productdetail'),

    path('clearance/<str:slug>',ClearanceTemplateView.as_view(), name='clearance'),
    
    path('newarrivals/', NewArrival.as_view(), name='newarrival'),


    #--------------------------------footer quicklinks---------------------------------------------

    path('shipping-policy/', quicklinks.Shipping, name="shipping"),
    path('returns-policy/', quicklinks.Return, name="returns"),
    path('privacy-policy/',quicklinks.PrivacyPolicy, name="privacy"),
    path('terms&conditions/',quicklinks.TermsAndConditions, name="terms"),






    
    #----------------------------------------passwords reset links----------------------------------------------


    # path('password_reset/', auth_views.PasswordResetView.as_view(
    #     template_name='users/password_reset.html'), name='password_reset'),

    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
    #     template_name='users/password_reset_done.html'), name='password_reset_done'),

    #path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),

    # --------------------------------------------------end of password reser links---------------------------------------

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)