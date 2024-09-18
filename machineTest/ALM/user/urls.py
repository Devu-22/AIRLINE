from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('user/register/', views.admin_register, name='admin_register'),
    path('user/login/', views.admin_login, name='admin_login'),
    path('user/logout/', views.admin_logout, name='admin_logout'),
    path('user/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('user/', views.flight_list, name='flight_list'),
    path('user/search/', views.flight_search, name='flight_search'),
    path('user/add/', views.add_flight, name='add_flight'),
    path('user/edit/<str:flight_id>/', views.edit_flight, name='edit_flight'),
    path('edit_flight_main/', views.edit_flight_main, name='edit_flight_main'),
]
