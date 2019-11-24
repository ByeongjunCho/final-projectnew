from django.shortcuts import render,redirect,get_object_or_404
from .forms import CustomUserCreationForm,CustomUserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from .models import User
from django.contrib.auth.decorators import login_required




def indexs(request):
    Users = User.objects.all()
    context = {
        'Users':Users
    }
    return render(request,'accounts/indexs.html',context)

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form
    }
    return render(request,'accounts/signup.html',context)
    
def login(request):
    if request.user.is_authenticated:
        return redirect('movies:index')
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request,user)
            return redirect('movies:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request,'accounts/login.html',context)

def logout(request):
    auth_logout(request)
    return redirect('movies:index')

def profile(request, account_pk):
    User = get_user_model()
    user = get_object_or_404(User,pk=account_pk)
    context = {
        'user_profile':user
    }
    return render(request,'accounts/profile.html',context)

def follow(request, account_pk):
    User = get_user_model()
    obama = get_object_or_404(User,pk=account_pk)
    if obama != request.user:
        if request.user in obama.followers.all():
            obama.followers.remove(request.user)
        else:
            obama.followers.add(request.user)
        return redirect('accounts:profile',account_pk)

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('movies:index')
    else:
        form = PasswordChangeForm(request.user) # 반드시 첫번째 인자로 user
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)