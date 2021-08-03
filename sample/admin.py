from django.contrib import admin

#メインリストインポート
from .models import MainList
#サブリストインポート
from .models import SubList

#メイン・サブリストを管理画面上に表示
admin.site.register(MainList)
admin.site.register(SubList)