from django.db import models
from django.utils import timezone
 
class Message(models.Model):
    # クラス変数で、カラムを定義
    # name カラム
    name = models.CharField("お名前", max_length=20)
    # body カラム
    body = models.CharField("本文", max_length=100)
    # created_at カラム
    created_at = models.DateTimeField("作成日", default=timezone.now)
 
    def __str__(self):
        return f"name: {self.name} body: {self.body}"