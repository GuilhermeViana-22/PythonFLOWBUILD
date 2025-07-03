from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Position


@login_required
def positions(request):
    positions = Position.objects.all()
    return render(request, 'positions/positions.html', {'positions': positions})


@login_required
def position_edit(request, position_id):
    position = get_object_or_404(Position, pk=position_id)
    if request.method == 'POST':
        position.name = request.POST.get('name')
        position.description = request.POST.get('description')
        position.save()
        return redirect('positions')
    return render(request, 'positions/position_edit.html', {'position': position})
