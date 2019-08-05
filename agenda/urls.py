from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('event/<int:id>', views.read, name='read'),
]