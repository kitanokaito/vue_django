from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserList.as_view()),
    path('create-users/', UserCreate.as_view()),
    path('store/', StoreListCreate.as_view()),
    path('users/<pk>/', UserRetrieveUpdate.as_view())
]