from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import DashboardUser


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
    return render(request, 'users/users_all.html', context)


@login_required
def user_detail(request, user_id):
    user = get_object_or_404(DashboardUser, pk=user_id)
    return render(request, 'users/user_detail.html', {'user': user})


@login_required
def user_delete(request, user_id):
    user = get_object_or_404(DashboardUser, pk=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('users_all')
    return render(request, 'users/user_confirm_delete.html', {'user': user})
