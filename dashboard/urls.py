from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard'),
    path('users/all/', views.users_all, name='users_all'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('users/<int:user_id>/delete/', views.user_delete, name='user_delete'),
    path('users/roles/', views.users_roles, name='users_roles'),
    path('users/roles/<int:role_id>/edit/', views.role_edit, name='role_edit'),
    path('users/permissions/', views.users_permissions, name='users_permissions'),
    path('users/permissions/<int:permission_id>/edit/', views.permission_edit, name='permission_edit'),
    path('positions/', views.positions, name='positions'),
    path('positions/<int:position_id>/edit/', views.position_edit, name='position_edit'),
    path('flow/builder/', views.flow_builder, name='flow_builder'),
    path('flow/templates/', views.flow_templates, name='flow_templates'),
    path('flow/integrations/', views.flow_integrations, name='flow_integrations'),
    path('interpreter/', views.interpreter, name='interpreter'),
    path('history/', views.history, name='history'),
    path('settings/general/', views.settings_general, name='settings_general'),
    path('settings/security/', views.settings_security, name='settings_security'),
    path('settings/notifications/', views.settings_notifications, name='settings_notifications'),
    path('tasks/', views.tasks, name='tasks'),
    path('profile/', views.profile, name='profile'),
    path('configurations/', views.configurations, name='configurations'),
]
