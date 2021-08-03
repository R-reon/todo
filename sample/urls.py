from django.urls import path
#ビューインポート
from . import views

app_name = 'sample'
urlpatterns = [
    #ビューのindex関数読み込み
    path('', views.index, name='index'),
    #ビューのメイン・サブリスト関数読み込み(項目名で動的に切り替え)
    path('mainlist/<str:listname>/', views.main_list, name='mainlist'),
    path('sublist/<str:listname>/', views.sub_list, name='sublist')
]