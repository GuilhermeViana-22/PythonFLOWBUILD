from django.urls import path
from . import views

urlpatterns = [
    path('general/', views.settings_general, name='settings_general'),
    path('security/', views.settings_security, name='settings_security'),
    path('notifications/', views.settings_notifications, name='settings_notifications'),
] 