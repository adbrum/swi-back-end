from django.urls import path
from . import views

urlpatterns = [
    path('list/<int:pk>/', views.leadList, name='list'),
    path('create/', views.leadCreate, name='create'),
]
