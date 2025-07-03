from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Role, CustomPermission


@login_required
def users_roles(request):
    roles = Role.objects.all()
    return render(request, 'permissions/users_roles.html', {'roles': roles})


@login_required
def role_edit(request, role_id):
    role = get_object_or_404(Role, pk=role_id)
    if request.method == 'POST':
        role.name = request.POST.get('name')
        role.description = request.POST.get('description')
        role.save()
        return redirect('users_roles')
    return render(request, 'permissions/role_edit.html', {'role': role})


@login_required
def users_permissions(request):
    permissions = CustomPermission.objects.all()
    return render(request, 'permissions/users_permissions.html', {'permissions': permissions})


@login_required
def permission_edit(request, permission_id):
    permission = get_object_or_404(CustomPermission, pk=permission_id)
    if request.method == 'POST':
        permission.name = request.POST.get('name')
        permission.code = request.POST.get('code')
        permission.description = request.POST.get('description')
        permission.save()
        return redirect('users_permissions')
    return render(request, 'permissions/permission_edit.html', {'permission': permission})
