from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login_view')
    else:
        user_form = CustomUserCreationForm()
    context = {
        'user_form': user_form
    }
    return render(request, 'accounts/register.html', context=context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('cars_view')
        else:
            login_form = CustomAuthenticationForm(request.POST)
    else:
        login_form = CustomAuthenticationForm()
    context = {
        'login_form': login_form
    }
    return render(request, 'accounts/login.html', context=context)

def logout_view(request):
    logout(request)
    return redirect('cars_view')
