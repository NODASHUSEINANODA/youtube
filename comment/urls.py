from django.urls import path
from django.shortcuts import render
 
# 同じディレクトリの views.py をインポート
from . import views
 
# 各ルーティングの関数名に views. を付加
urlpatterns = [
    path("simple/", views.simple), 
    path("other/", views.other),
    path("total/", views.total),
    path("template_sample/", views.template_sample),
    path("template_context_sample/", views.template_context_sample),
    path("template_example/", views.template_example),
    path("top_sample/", views.top_sample),
    path("user_sample/", views.user_sample),
    path("privacy_sample/", views.privacy_sample),
    path("login_sample/", views.login_sample),
    path("signup_sample/", views.signup_sample),
    # その他課題で作成したルーティング
    path("show_profile/", views.show_profile),
    path("get_post_sample/", views.get_post_sample), # 追記
    path("url_parameter_sample/<int:id>", views.url_parameter_sample), # 追記
    path("url_parameter_sample/<int:id>/comments/<int:comment_id>/", views.url_parameter_sample), # 追記
    path("show_item/<int:id>/", views.show_item), # 追記
    path("model_sample/", views.model_sample),
    path("index/", views.message_list),
    path("message_detail/<int:id>/", views.message_detail),
    path("message_delete/<int:id>/", views.message_delete),
    path("message_create/", views.message_create),
    path("message_update/<int:id>/", views.message_update),
]