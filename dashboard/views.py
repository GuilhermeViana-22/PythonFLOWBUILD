from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import DashboardUser


@login_required
def dashboard_home(request):
    return render(request, 'dashboard/dashboard.html')


@login_required
def users_all(request):
    query = request.GET.get('q', '')
    users = DashboardUser.objects.all()
    if query:
        users = users.filter(name__icontains=query)
    paginator = Paginator(users, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'users': page_obj, 'query': query}
    return render(request, 'dashboard/users_all.html', context)


@login_required
def user_detail(request, user_id):
    user = get_object_or_404(DashboardUser, pk=user_id)
    return render(request, 'dashboard/user_detail.html', {'user': user})


@login_required
def user_delete(request, user_id):
    user = get_object_or_404(DashboardUser, pk=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('users_all')
    return render(request, 'dashboard/user_confirm_delete.html', {'user': user})


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
