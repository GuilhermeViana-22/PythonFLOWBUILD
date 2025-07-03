from django.urls import path
from . import views

urlpatterns = [
    path('builder/', views.flow_builder, name='flow_builder'),
    path('templates/', views.flow_templates, name='flow_templates'),
    path('integrations/', views.flow_integrations, name='flow_integrations'),
] 