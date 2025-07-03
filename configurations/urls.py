from django.urls import path
from . import views

urlpatterns = [
    path('', views.configurations, name='configurations'),
] 