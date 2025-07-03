from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import datetime, timedelta
import json


def login_view(request):
    """View para página de login"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Credenciais inválidas. Tente novamente.')
        else:
            messages.error(request, 'Por favor, preencha todos os campos.')
    
    return render(request, 'accounts/login.html')


def register_view(request):
    """View para página de registro"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if username and email and password1 and password2:
            if password1 != password2:
                messages.error(request, 'As senhas não coincidem.')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Nome de usuário já existe.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email já cadastrado.')
            else:
                try:
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        password=password1
                    )
                    messages.success(request, 'Conta criada com sucesso! Faça login.')
                    return redirect('login')
                except Exception as e:
                    messages.error(request, f'Erro ao criar conta: {str(e)}')
        else:
            messages.error(request, 'Por favor, preencha todos os campos.')
    
    return render(request, 'accounts/signup.html')


def password_reset_view(request):
    """View para recuperação de senha"""
    if request.method == 'POST':
        email = request.POST.get('email')
        
        if email:
            try:
                user = User.objects.get(email=email)
                # Aqui você pode implementar o envio de email
                # Por enquanto, vamos apenas mostrar uma mensagem de sucesso
                messages.success(request, 'Instruções para recuperação de senha foram enviadas para seu email.')
                return redirect('login')
            except User.DoesNotExist:
                messages.error(request, 'Nenhum usuário encontrado com este email.')
        else:
            messages.error(request, 'Por favor, digite seu email.')
    
    return render(request, 'authentication/password_reset.html')


@login_required
def dashboard_view(request):
    """View para dashboard - requer autenticação"""
    now = datetime.now()
    
    # Dados simulados para recent_users
    recent_users = [
        {
            'name': 'João Silva',
            'avatar': 'https://via.placeholder.com/40',
            'join_date': '2 days ago',
            'status': 'Active'
        },
        {
            'name': 'Maria Santos',
            'avatar': 'https://via.placeholder.com/40',
            'join_date': '1 day ago',
            'status': 'Active'
        },
        {
            'name': 'Pedro Lima',
            'avatar': 'https://via.placeholder.com/40',
            'join_date': '3 days ago',
            'status': 'Inactive'
        },
        {
            'name': 'Ana Costa',
            'avatar': 'https://via.placeholder.com/40',
            'join_date': '1 hour ago',
            'status': 'Active'
        },
    ]
    
    # Dados simulados para recent_activities
    recent_activities = [
        {
            'user': {
                'name': 'João Silva',
                'email': 'joao@email.com',
                'avatar': 'https://via.placeholder.com/40'
            },
            'action': 'User Login',
            'details': 'Logged in successfully',
            'ip': '192.168.1.100',
            'time': '2 min ago'
        },
        {
            'user': {
                'name': 'Maria Santos',
                'email': 'maria@email.com',
                'avatar': 'https://via.placeholder.com/40'
            },
            'action': 'Profile Update',
            'details': 'Updated profile information',
            'ip': '192.168.1.101',
            'time': '5 min ago'
        },
        {
            'user': {
                'name': 'Pedro Lima',
                'email': 'pedro@email.com',
                'avatar': 'https://via.placeholder.com/40'
            },
            'action': 'Password Change',
            'details': 'Changed password',
            'ip': '192.168.1.102',
            'time': '10 min ago'
        },
    ]
    
    context = {
        'user': request.user,
        'username': request.user.username,
        'email': request.user.email,
        'current_date': now.strftime('%B %d, %Y'),
        'current_time': now.strftime('%I:%M %p'),
        'recent_users': recent_users,
        'recent_activities': recent_activities,
    }
    return render(request, 'dashboard/dashboard.html', context)


def logout_view(request):
    """View para logout"""
    auth_logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('welcome')


@csrf_exempt
@require_http_methods(["POST"])
def api_login(request):
    """API endpoint para login com JWT"""
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return JsonResponse({'error': 'Username e password são obrigatórios'}, status=400)
        
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return JsonResponse({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
                'user_id': user.id,
                'username': user.username,
                'email': user.email,
            })
        else:
            return JsonResponse({'error': 'Credenciais inválidas'}, status=401)
    
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON inválido'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
