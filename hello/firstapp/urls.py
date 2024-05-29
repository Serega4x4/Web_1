from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^contact/', views.contact),
    re_path(r'^about/', views.about),
    path('products/', views.products),
    path('products/<int:productid>/', views.products),
    path('users/<int:id>/<name>/', views.users),
    path('users/', views.users),
    path('', views.index, name='index'),
]
