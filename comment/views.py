from django.shortcuts import render, redirect
from django.http import HttpResponse
# モデルをインポート
from .models import Message

# フォームをインポート
from .forms import MessageCreateForm

# simple メソッドを定義
def simple(request):
    # レスポンスを返す関数
    return HttpResponse("シンプルなルーティング！")
 
def other(request):
    return HttpResponse("ここはother/です。")
 
def total(request):
    total = 0
    for i in range(1, 10 + 1):
        total += i
    return HttpResponse(f"1から10 までの合計は{total}です。")
 
def template_sample(request):
    return render(request, "comment/sample.html", {})
 
def template_context_sample(request):
    title = "テンプレートのサンプルです"
    description = "テンプレートを利用すると、<br>HTML 内に Python の変数を埋め込むことができます。"
    return render(request, "comment/template_context.html", {
        "title" : title,
        "description" : description,
        "direct" : "辞書に直接文字列を書いても問題ありません。"
    })
 
def template_example(request):
    title = "テンプレートの様々な機能"
    num = 10
    names = ["山田", "山本", "鈴木", "佐藤", "田中"]
    return render(request, "comment/template_example.html", {
        "title" : title,
        "num" : num,
        "names" : names,
    })
 
def top_sample(request):
    return render(request, "comment/top_sample.html", {
        "title" : "トップページ",
    })
 
def user_sample(request):
    return render(request, "comment/user_sample.html", {
        "title" : "ユーザー設定",
    })
 
def privacy_sample(request):
    return render(request, "comment/privacy_sample.html", {
        "title" : "プライバシーポリシー",
    })
 
def login_sample(request):
    return render(request, "comment/login_sample.html", {
        "title" : "ログイン",
    })
 
 
def signup_sample(request):
    return render(request, "comment/signup_sample.html", {
        "title" : "サインアップ",
    })
 
# その他課題で作成したビュー関数

def show_profile(request):
    return render(request, "comment/show_profile.html", {
        "title" : "サインアップ",
    })
    
def get_post_sample(request):
    return render(request, "comment/get_post_sample.html", {
        "title" : "GETとPOSTのサンプル",
        "request_method" : request.method,
        "get_values": request.GET,
        "post_values" : request.POST,
    })
    
def url_parameter_sample(request, id, comment_id):
    return render(request, "comment/url_parameter_sample.html", {
        "title" : "URLパラメーターのサンプル",
        "id" : id,
        "comment_id" : comment_id,
    })
    
def show_item(request, id, comment_id, price_id, item_name_id):
    return render(request, "comment/show_item.html", {
        "title" : "課題：ルーティングパラメータ",
        "id" : id,
        "item_name_id" : item_name_id,
        "price_id" : price_id,
    })
    
def model_sample(request):
    message = Message.objects.get(id=2)
    return render(request, "comment/model_sample.html", {
        "title" : "モデルの使いかた",
        "message" : message,
    })

def message_list(request):
    messages = Message.objects.all()
    return render(request, "comment/index.html", {
        "title" : "一言掲示板",
        "messages" : messages,
    })
    
def message_detail(request, id):
    message = Message.objects.get(id=id)
    return render(request, "comment/message_detail.html", {
        "title" : f"id: {id} のメッセージ",
        "message" : message,
    })
    
def message_update(request, id):
    message = Message.objects.get(id=id)
    # フォーム送信時の処理
    if request.method == "POST":
        # name と comment をフォームの値から更新
        message.name = request.POST.get("name")
        message.body = request.POST.get("body")
        # Message インスタンスを保存
        message.save()
        # 詳細ページへリダイレクト
        return redirect(f"/comment/message_detail/{message.id}")
 
    return render(request, "comment/message_update.html", {
        "title" : f"id: {id} のメッセージ",
        "message" : message,
    })

def message_delete(request, id):
    if request.method == "POST":
        message = Message.objects.get(id=id)
        message.delete()
 
    # 一覧ページへリダイレクト
    return redirect("/comment/index/")
    
def message_create(request):
    # フォーム送信時の処理
    if request.method == "POST":
        # メッセージインスタンスを生成
        message = Message()
        # name と comment をフォームの値から設定
        message.name = request.POST.get("name")
        message.body = request.POST.get("body")
        # Message インスタンスを保存
        message.save()
        # 一覧ページへリダイレクト
        return redirect("/comment/index/")
 
    return render(request, "comment/message_create.html", {
        "title" : "新規投稿",
    })
    
def message_create(request):
    # フォームインスタンスを作成
    form = MessageCreateForm(request.POST or None)
    # フォーム送信時の処理
    if request.method == "POST":
        # メッセージインスタンスを生成
        message = Message()
        # name と comment をフォームの値から設定
        message.name = request.POST.get("name")
        message.body = request.POST.get("body")
        # Message インスタンスを保存
        message.save()
        # 一覧ページへリダイレクト
        return redirect("/comment/index/")
 
    return render(request, "comment/message_create.html", {
        "title" : "新規投稿",
        "form" : form, # テンプレートにフォームインスタンスを渡す
    })
    
def message_create(request):
    # フォームインスタンスを作成
    form = MessageCreateForm(request.POST or None)
    # フォームの入力が不正でないかチェック(is_valid)
    if request.method == "POST" and form.is_valid():
        message = Message()
        # フォームインスタンスから name と body を取得
        message.name = form.cleaned_data.get("name")
        message.body = form.cleaned_data.get("body")
        message.save()
        return redirect("/comment/index/")
 
    return render(request, "comment/message_create.html", {
        "title" : "新規投稿",
        "form" : form, # テンプレートにフォームインスタンスを渡す
    })
    
def message_create(request):
    form = MessageCreateForm(request.POST or None)
    # フォーム送信時の処理
    if request.method == "POST" and form.is_valid():
        # メッセージインスタンスを生成
        # message = Message()
        # フォームインスタンスから name と body を取得
        # message.name = form.cleaned_data.get("name")
        # message.body = form.cleaned_data.get("body")
        # Message インスタンスを保存
        # message.save()
        form.save()
        # 一覧ページへリダイレクト
        return redirect("/comment/index/")
 
    return render(request, "comment/message_create.html", {
        "title" : "新規投稿",
        "form" : form,
    })