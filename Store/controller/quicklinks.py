from django.shortcuts import render, redirect

def Shipping(request):
    return render(request, 'Store/shipping.html')



def Return(request):
    return render(request, 'Store/return.html')



def PrivacyPolicy(request):
    return render(request, 'Store/privacy.html')



def TermsAndConditions(request):
    return render(request, 'Store/t&c.html')