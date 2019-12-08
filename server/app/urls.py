from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<pk>/', UserRetrieveUpdate.as_view()),
    path('create-users/', UserCreate.as_view()),
    path('store/', StoreListCreate.as_view()),
    path('good/create/', GoodCreate.as_view()),
    path('good/destroy/<int:from_user>/<int:to_store>/', GoodDestroy.as_view()),
    path('good/num/', GoodNum.as_view()),
]