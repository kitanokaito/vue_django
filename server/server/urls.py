from django.contrib import admin
from django.urls import include, path
from django.conf import settings # 追加        
from django.conf.urls.static import static # 追加

from rest_framework_jwt.views import obtain_jwt_token # 追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', obtain_jwt_token), # 追加
    path('api/', include('app.urls'))
]

# メディアファイルの公開設定
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)