from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='index_login'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register_user/', views.register_user, name='register_user'),
    path('register_contact/', views.register_contact, name='register_contact')
]
