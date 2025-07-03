from django.urls import path
from . import views

urlpatterns = [
    path('', views.positions, name='positions'),
    path('<int:position_id>/edit/', views.position_edit, name='position_edit'),
] 