from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == "POST":
        data =request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        profile_image = request.FILES.get('profile_image')
        address = data.get('address')
        user_type = data.get('user_type')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
       
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already taken')
            return redirect('/register/')
        
        user = User.objects.create_user(username=username, password=password)
        
        person = Person.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            profile_image=profile_image,
            address=address,
            user_type=user_type,
        )
        
        messages.info(request, 'Account created successfully')
        return redirect('/register/')
    
    return render(request, 'register.html')

def login_view(request):
    if request.method=="POST":
        
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        if not User.objects.filter(username=username).exists():
            messages.info(request,'Invalid Username')
            return redirect('/login/')

        user = authenticate(request, username = username, password=password)
        if user is None:
            messages.info(request,'Invalid Password')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/dashboard/')
            
    
    return render(request, 'login.html')


@login_required
def dashboard(request):
    person = Person.objects.get(user=request.user)
    
    context = {
        'person': person,
        'username': request.user.username,
        'user_type': person.user_type,  
        
    }
    return render(request, 'dashboard.html', context)