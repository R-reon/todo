from django.http import HttpResponse
from django.shortcuts import render
#モデルインポート
from .models import MainList
from .models import SubList

def index(request):
    #/sampleに表示する文字列設定
    return HttpResponse("サンプルページ!!")

def main_list(request, listname):
    #メインリスト取得
    mainlist = MainList.objects.filter(title=listname)
    context = {
        'title': listname,
        'mainlist': mainlist
        }
    return render(request, 'sample/main_list.html', context)

def sub_list(request, listname):
    #サブリスト取得
    sublist = SubList.objects.filter(title=listname)
    context = {
        'title': listname,
        'sublist': sublist
        }
    return render(request, 'sample/sub_list.html', context)