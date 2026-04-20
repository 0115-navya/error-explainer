from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('history/', views.history_view, name='history'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]