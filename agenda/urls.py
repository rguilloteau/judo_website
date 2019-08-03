from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('event/<int:id>', views.read, name='read'),
]