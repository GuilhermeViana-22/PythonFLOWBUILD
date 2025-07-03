from django.urls import path
from . import views

urlpatterns = [
    path('', views.interpreter, name='interpreter'),
] 