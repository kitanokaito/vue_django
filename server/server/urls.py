from django.contrib import admin
from django.urls import include, path
# from django.conf.urls import include

from rest_framework_jwt.views import obtain_jwt_token # 追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', obtain_jwt_token), # 追加
    path('api/', include('app.urls'))
]
