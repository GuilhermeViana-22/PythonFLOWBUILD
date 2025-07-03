from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.conf import settings
from pathlib import Path
import difflib

from .models import DashboardUser, Position, Role, CustomPermission


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
    roles = Role.objects.all()
    return render(request, 'dashboard/users_roles.html', {'roles': roles})


@login_required
def role_edit(request, role_id):
    role = get_object_or_404(Role, pk=role_id)
    if request.method == 'POST':
        role.name = request.POST.get('name')
        role.description = request.POST.get('description')
        role.save()
        return redirect('users_roles')
    return render(request, 'dashboard/role_edit.html', {'role': role})


@login_required
def users_permissions(request):
    permissions = CustomPermission.objects.all()
    return render(request, 'dashboard/users_permissions.html', {'permissions': permissions})


@login_required
def permission_edit(request, permission_id):
    permission = get_object_or_404(CustomPermission, pk=permission_id)
    if request.method == 'POST':
        permission.name = request.POST.get('name')
        permission.code = request.POST.get('code')
        permission.description = request.POST.get('description')
        permission.save()
        return redirect('users_permissions')
    return render(request, 'dashboard/permission_edit.html', {'permission': permission})


@login_required
def positions(request):
    positions = Position.objects.all()
    return render(request, 'dashboard/positions.html', {'positions': positions})


@login_required
def position_edit(request, position_id):
    position = get_object_or_404(Position, pk=position_id)
    if request.method == 'POST':
        position.name = request.POST.get('name')
        position.description = request.POST.get('description')
        position.save()
        return redirect('positions')
    return render(request, 'dashboard/position_edit.html', {'position': position})


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
    media_root = Path(settings.BASE_DIR) / 'media'
    media_root.mkdir(exist_ok=True)
    file_names = sorted([f.name for f in media_root.glob('*.json')])
    file_a = request.GET.get('file_a') or (file_names[0] if file_names else None)
    file_b = request.GET.get('file_b') or (file_names[1] if len(file_names) > 1 else None)

    lines_a = []
    lines_b = []
    removed = set()
    added = set()

    if file_a and file_b:
        path_a = media_root / file_a
        path_b = media_root / file_b
        if path_a.exists() and path_b.exists():
            lines_a = path_a.read_text().splitlines()
            lines_b = path_b.read_text().splitlines()
            diff = list(difflib.ndiff(lines_a, lines_b))
            removed = {line[2:] for line in diff if line.startswith('- ')}
            added = {line[2:] for line in diff if line.startswith('+ ')}

    context = {
        'file_names': file_names,
        'file_a': file_a,
        'file_b': file_b,
        'lines_a': [{'text': line, 'removed': line in removed} for line in lines_a],
        'lines_b': [{'text': line, 'added': line in added} for line in lines_b],
    }
    return render(request, 'dashboard/history.html', context)


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


@login_required
def profile(request):
    profile = getattr(request.user, 'profile', None)
    if request.method == 'POST':
        request.user.first_name = request.POST.get('name')
        request.user.email = request.POST.get('email')
        request.user.save()
        if profile:
            profile.phone = request.POST.get('phone')
            profile.save()
        return redirect('profile')
    return render(request, 'dashboard/profile.html', {'profile': profile})


@login_required
def configurations(request):
    return render(request, 'dashboard/configurations.html')
