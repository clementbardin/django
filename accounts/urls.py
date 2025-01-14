from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('login_user/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register_user/', views.register_user, name='register'),
]