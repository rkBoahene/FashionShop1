from django.shortcuts import render

# Create your views here.
def about_company(request):
    return render(request,"shop/about.html")


def contact_us(request):
    return render(request,"shop/contact.html")