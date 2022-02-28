from django.urls import path

from . import views

urlpatterns = [
    path('', views.getMovie, name='index'),
]