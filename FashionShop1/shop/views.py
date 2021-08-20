from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, get_user_model
from .forms import LoginForm,RegisterForm
# Create your views here.
def welcomePage(request):
    return render(request,'shop/index.html')


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            # refresh form fields
            # context['form'] = LoginForm()
            return redirect("/")
        else:
            print('Error')
            pass
    return render(request,'auth/login.html',context)

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
        print(new_user)
    return render(request,'auth/register.html',context)