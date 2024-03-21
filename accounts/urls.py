from . import views
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),
    path('dashboard/', views.dashboard,name='dashboard'),
    path('register/', views.register,name='register'),
    
        
]