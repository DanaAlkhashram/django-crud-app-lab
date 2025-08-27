# my_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('items/', views.item_list, name='item_list'),
    path('items/<int:pk>/', views.item_detail, name='item_detail'),
    path('items/create/', views.ItemCreate.as_view(), name='item_create'),
    path('items/<int:pk>/update/', views.ItemUpdate.as_view(), name='item_update'),
    path('items/<int:pk>/delete/', views.ItemDelete.as_view(), name='item_delete'),
]
