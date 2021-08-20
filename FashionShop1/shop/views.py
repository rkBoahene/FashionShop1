from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
# Create your views here.
def welcomePage(request):
    return render(request,'base.html')


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
            return redirect("/mylogin")
        else:
            print('Error')
            pass
    return render(request,'auth/login.html',context)

def register_page(request):
    return render(request,'auth/register.html')