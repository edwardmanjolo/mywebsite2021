from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='site99-home'),
    path('about/', views.about, name='site99-about'),
    path('contact/', views.contact, name='site99-contact'),
]
