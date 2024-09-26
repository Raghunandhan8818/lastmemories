from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from user.models import User, Plan, File, MemorialProfile


# Create your views here.

def signup(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']
        if password != confirm_password:
            messages.error(request, 'Passwords must match')
            return render(request, 'signup.html')
        if User.objects.filter(username=request.POST['email']).exists():
            messages.error(request, 'Email already registered')
            return render(request, 'signup.html')
        fullname = request.POST['full_name']
        mobile = request.POST['mobile_number']
        user = User.objects.create(username=email, email=email, mobile_number=mobile, fullname=fullname)
        user.set_password(password)
        user.save()
        messages.success(request, 'Your account has been created!, Please Log In')
        return redirect("login")
    return render(request, "./signup.html")


def user_login(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect("home")
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html')
    return render(request, "./login.html")


def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect("login")


@login_required(login_url='login')
def home(request):
    user = User.objects.get(username=request.user.username)
    plans = Plan.objects.all()
    memorials = MemorialProfile.objects.filter(associated_memorial_profile__user=request.user)
    print(memorials)
    context = {"fullname": user.fullname, "plans": plans, "associated_memorial_profiles": memorials}

    return render(request, "./home.html", context=context)
