from django.contrib import admin
from django.urls import path, include # include を追記
 
# 関数をすべて削除
 
# sample.urls に移動したルーティングを削除
urlpatterns = [
    path("admin/", admin.site.urls),
    path("sample/", include("sample.urls")), # 追記
    path("comment/", include("comment.urls")), # 追記
]