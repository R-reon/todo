from django.db import models

#メインリストテーブル
class MainList(models.Model):
    class Meta:
        #テーブル名設定
        db_table = 'mainlist'

    #フィールド設定(メイン項目名、日付)
    title = models.CharField(verbose_name='メイン項目名', max_length=100)
    datetime = models.DateTimeField(verbose_name='日付')

    #名称設定
    def __str__(self):
        return self.title

#サブリストテーブル
class SubList(models.Model):
    class Meta:
        #テーブル名設定
        db_table = 'sublist'

    #フィールド設定(サブ項目名、総数)
    mainlist = models.ForeignKey(MainList, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='サブ項目名', max_length=100)
    totalnum = models.IntegerField(verbose_name='総数', default=0)

    #名称設定
    def __str__(self):
        return self.title