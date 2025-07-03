from django.shortcuts import render

# Create your views here.

def welcome(request):
    """View para a página welcome"""
    return render(request, 'welcome/welcome.html')
