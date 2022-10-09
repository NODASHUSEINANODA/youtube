from django.contrib import admin
 
# Message モデルをインポート
from .models import Message
 
# Message モデルを管理サイトに登録
admin.site.register(Message)