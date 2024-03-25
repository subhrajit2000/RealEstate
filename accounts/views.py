from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from Urbanacre.models import CustomUser

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        # Validate password complexity 
        if not (any(char.isupper() for char in password1) and
                any(char.islower() for char in password1) and
                any(char.isdigit() for char in password1) and
                len(password1) >= 8):
            messages.info(request, 'Password must contain at least one uppercase letter, one lowercase letter, one digit, and be at least 8 characters long')
            return redirect('register')
           
        if password1 != password2:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
        
        if CustomUser.objects.filter(email=email).exists():
            messages.info(request, 'Email already exists')
            return redirect('register')
        
        if CustomUser.objects.filter(phone_number=phone_number).exists():
            messages.info(request, 'Phone number already exists')
            return redirect('register')
        
        try:
            user = CustomUser.objects.create_user(email=email, password=password1, name=name, phone_number=phone_number)
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')
        except Exception as e:
            messages.error(request, 'An error occurred during registration. Please try again later.')
            return redirect('register')
    else:
        return render(request, 'register.html')
    

def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'login.html') 



def logout(request):
    logout(request)
    return redirect('/')
  