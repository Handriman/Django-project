from django.urls import path
from . import views

urlpatterns = [
    path('', views.grapes_home, name='grapes_home'),

]