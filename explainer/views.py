from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import ErrorExplanation
from .utils import explain_error, detect_language, detect_severity

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        email = request.POST.get('email', '').strip()
        
        if not username or not password:
            messages.error(request, 'Username and password are required!')
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken!')
            return redirect('register')
        
        user = User.objects.create_user(username=username, password=password, email=email)
        login(request, user)
        return redirect('home')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        messages.error(request, 'Invalid credentials!')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')


def home_view(request):
    if not request.user.is_authenticated:
        return render(request, 'landing.html')
    if request.method == 'POST':
        error_text = request.POST.get('error_text', '').strip()
        
        if not error_text:
            messages.error(request, 'Please paste an error first!')
            return redirect('home')
            
        language = detect_language(error_text)
        severity = detect_severity(error_text)
        explanation = explain_error(error_text)
        ErrorExplanation.objects.create(
            user=request.user,
            error_text=error_text,
            language=language,
            severity=severity,
            explanation=explanation
        )
        return render(request, 'home.html', {
            'explanation': explanation,
            'language': language,
            'severity': severity,
            'error_text': error_text
        })
    return render(request, 'home.html')

@login_required(login_url='login')
def history_view(request):
    errors = ErrorExplanation.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'history.html', {'errors': errors})
