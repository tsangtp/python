from django.urls import path
from . import views

urlpatterns = [
    path('',views.sign_in,name='Login'),
    path('register', views.sign_up, name='Register'),
    path('index', views.index, name='Index'),
    path('logout', views.log_out, name='Logout')
]
