from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='Home'),
    path('update/<str:pk>', views.update, name='Update'),
    path('delete/<str:pk>', views.delete, name='Delete'),
    path('add/', views.add, name='Add'),
    path('search/', views.search, name='Search'),
]
