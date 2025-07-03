from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_home(request):
    return render(request, 'dashboard/dashboard.html')

@login_required
def users_all(request):
    return render(request, 'dashboard/users_all.html')

@login_required
def users_roles(request):
    return render(request, 'dashboard/users_roles.html')

@login_required
def users_permissions(request):
    return render(request, 'dashboard/users_permissions.html')

@login_required
def positions(request):
    return render(request, 'dashboard/positions.html')

@login_required
def flow_builder(request):
    return render(request, 'dashboard/flow_builder.html')

@login_required
def flow_templates(request):
    return render(request, 'dashboard/flow_templates.html')

@login_required
def flow_integrations(request):
    return render(request, 'dashboard/flow_integrations.html')

@login_required
def interpreter(request):
    return render(request, 'dashboard/interpreter.html')

@login_required
def history(request):
    return render(request, 'dashboard/history.html')

@login_required
def settings_general(request):
    return render(request, 'dashboard/settings_general.html')

@login_required
def settings_security(request):
    return render(request, 'dashboard/settings_security.html')

@login_required
def settings_notifications(request):
    return render(request, 'dashboard/settings_notifications.html')

@login_required
def tasks(request):
    return render(request, 'dashboard/tasks.html')
