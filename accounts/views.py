from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm, LoginForm


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')


class EmailLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
