from django.urls import path
from . import views

urlpatterns = [
    path('roles/', views.users_roles, name='users_roles'),
    path('roles/<int:role_id>/edit/', views.role_edit, name='role_edit'),
    path('permissions/', views.users_permissions, name='users_permissions'),
    path('permissions/<int:permission_id>/edit/', views.permission_edit, name='permission_edit'),
] 