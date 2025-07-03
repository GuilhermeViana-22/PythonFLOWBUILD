from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def configurations(request):
    return render(request, 'configurations/configurations.html')
