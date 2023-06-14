from django.shortcuts import render, redirect
from .forms import CustomUserForm, CustomLoginForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib import messages

def signup(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.exchange = request.POST.get('exchange')
            new_user.uid = request.POST.get('uid')
            new_user.upper_uid1 = request.POST.get('upper_uid1')
            new_user.is_active = False
            new_user.save()
            messages.success(request, '가입 성공! 첫 로그인시 관리자의 승인 이후에 이용 가능합니다.')
            auth_login(request, user=new_user)
            return redirect('accounts:login')
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