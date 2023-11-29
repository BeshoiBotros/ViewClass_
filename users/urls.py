# users/urls.py
from django.urls import path
from .views import UserView

urlpatterns = [
    path('users/', UserView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserView.as_view(), name='user-detail'),
]
