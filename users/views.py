from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, You logged in")
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
        
    context = {
        'title': 'Home - autorisation',
        'form': form
    }
    return render(request, 'users/login.html', context)


def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile successfully updated")
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'title': 'Home - profile',
        'form': form
    }
    return render(request, 'users/profile.html', context)


def reg(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"{user.username}, You registered and loged in")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Home - regestration',
        'form': form
    }
    return render(request, 'users/reg.html', context)

def logout(request):
    messages.success(request, f"{request.user.username}, You logged out")
    auth.logout(request)
    return redirect(reverse('main:index'))

def users_cart(request):
    return render(request, 'users/users_cart.html')