# coding=utf-8

from django.urls import path

from . import views

urlpatterns = [
    path('', views.default_view),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('register/', views.register_view),
    path('index/', views.index_view),
    path('index/buy/', views.buy_view),
    path('index/airline/', views.airline_view),
    path('user/journey/', views.journey_view),
    path('user/update/', views.update_view),
    path('user/cpwd/', views.change_pwd_view),
    path('user/', views.user_view),
]
