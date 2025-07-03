from django.urls import path
from . import views

urlpatterns = [
    path('', views.users_all, name='users_all'),
    path('<int:user_id>/', views.user_detail, name='user_detail'),
    path('<int:user_id>/delete/', views.user_delete, name='user_delete'),
] 