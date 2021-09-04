from django.shortcuts import render

# Create your views here.
def cart_home(request):
    print(request.session.session_key)
    return render(request, "cart/home.html")