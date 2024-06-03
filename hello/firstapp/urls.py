from django.urls import path, re_path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

]
