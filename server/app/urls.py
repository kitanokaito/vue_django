from django.urls import path
from .views import *

urlpatterns = [
    path('store/', StoreListCreate.as_view()),
    path('store/user', StoreListOfUser.as_view()),
    path('good/', GoodCreate.as_view()),
    path('good/<store_id>', GoodDestroy.as_view()),
]