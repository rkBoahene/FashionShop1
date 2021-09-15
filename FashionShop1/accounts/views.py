from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.utils.http import is_safe_url

from .forms import GuestForm, LoginForm,RegisterForm
from .models import GuestEmail

def guest_login_view(request):
    form = GuestForm(request.POST or None)
    context = {
        'form': form
    }
    # get redirect path to next page with any of these 2
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        email = form.cleaned_data.get("email")
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session["guest_email_id"] = new_guest_email.id
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("products:index")
       
    return render(request,'accounts/login.html',context)



def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    # get redirect path to next page with any of these 2
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
       
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
            # refresh form fields
            # context['form'] = LoginForm()
                return redirect("products:index")
        else:
           
            pass
    return render(request,'accounts/login.html',context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username,email,password)

    return render(request,'accounts/register.html',context)