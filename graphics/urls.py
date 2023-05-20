from django.urls import path
from . import views

urlpatterns = [
    path('', views.graphics_page, name='graphics_page'),
    path('create/', views.graphics_add, name='graphics_add'),
]
