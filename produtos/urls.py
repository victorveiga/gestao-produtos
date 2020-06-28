from django.contrib import admin
from django.urls import path
from .views import index, create, update, delete

urlpatterns = [
    path('', index, name='produtos'),
    path('new/', create, name='create_produto'),
    path('update/<int:id>', update, name='update_produto'),
    path('delete/<int:id>', delete, name='delete_produto'),
]
