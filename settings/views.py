from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def settings_general(request):
    return render(request, 'settings/settings_general.html')


@login_required
def settings_security(request):
    return render(request, 'settings/settings_security.html')


@login_required
def settings_notifications(request):
    return render(request, 'settings/settings_notifications.html')
