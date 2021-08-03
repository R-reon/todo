# from django.shortcuts import render
from rest_framework import viewsets
#モデルインポート
from sample.models import MainList
from sample.models import SubList
#シリアライズインポート
from .serializers import MainListSerializer
from .serializers import SubListSerializer

#メインリストビュー(GETのみ)
class MainListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MainList.objects.all()
    serializer_class = MainListSerializer

#サブリストビュー(GETのみ)
class SubListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SubList.objects.all()
    serializer_class = SubListSerializer