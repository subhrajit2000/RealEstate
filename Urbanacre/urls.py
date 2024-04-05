from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('property_list/', views.property_list, name='property_list'),
    path('property_details/<slug:slug>/', views.property_details, name='property_details'),
    path('addproperty/', views.addproperty, name='addproperty')
    ]