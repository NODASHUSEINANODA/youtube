
from django import forms
 
# Message モデルをインポート
from .models import Message
 
# ModelForm クラスを継承させる
class MessageCreateForm(forms.ModelForm):
    # クラス内に更に Meta クラスを定義する
    class Meta:
        # 利用するモデルは Message
        model = Message
        # created_at の入力欄は不要
        exclude = ("created_at",)
 
# # forms をインポート
# from django import forms
 
# # Form クラスを継承
# class MessageCreateForm(forms.Form):
#     # 作成したクラス変数が、フォームの各項目を表す
 
#     # name の入力フォームを作成
#     name = forms.CharField(
#         label="お名前", # label の文字列
#         required=True, # 必須か否か
#         widget=forms.TextInput() # 入力欄は type="text"
#     )
#     body = forms.CharField(
#         label="本文",
#         required=True,
#         widget=forms.TextInput()
#     )