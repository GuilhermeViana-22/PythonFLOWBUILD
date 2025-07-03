from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

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
    return render(request, 'user_profile/profile.html', {'profile': profile})
