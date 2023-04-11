from django.urls import path
from . import views

urlpatterns = [
    path('', views.grape_list, name='grape_list'),
    path('grape/<int:pk>/', views.grape_detail, name='grape_detail'),
]