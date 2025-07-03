from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def flow_builder(request):
    return render(request, 'flows/flow_builder.html')


@login_required
def flow_templates(request):
    return render(request, 'flows/flow_templates.html')


@login_required
def flow_integrations(request):
    return render(request, 'flows/flow_integrations.html')
