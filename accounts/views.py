from django.shortcuts import render, redirect
from .forms import CustomUserForm, CustomLoginForm
from django.contrib.auth import get_user_model
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.exchange = request.POST.get('exchange')
            new_user.uid = request.POST.get('uid')
            new_user.save()
            auth_login(request, user=new_user)
            return redirect('views:main')
    else:
        form = CustomUserForm()
    return render(request, 'accounts/signup.html', 
        {
            'form': form
        }
    )

def login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'views:main')
    else:
        form = CustomLoginForm()
    return render(request, 'accounts/login.html',
        {
            'form': form
        })

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')