from rest_framework import serializers
#モデルインポート
from sample.models import MainList
from sample.models import SubList

#メインリストシリアライザ
class MainListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainList
        #取得フィールド設定
        fields = ('title', 'datetime')

#サブリストシリアライザ
class SubListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubList
        #取得フィールド設定
        fields = ('title', 'totalnum')