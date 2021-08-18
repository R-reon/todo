from django.shortcuts import render, get_object_or_404, redirect #追加
from django.http import HttpResponse

from crud.models import Member
from crud.forms import MemberForm #追加

#一覧
def index(request):
    members = Member.objects.all().order_by('id') #値を取得
    return render(request, 'members/index.html', {'members':members}) #Templateに値を渡す
    
#新規と編集
def edit(request, id=None):

    if id: #idがあるとき（編集の時）
        #idで検索して、結果を戻すか、404エラー
        member = get_object_or_404(Member, pk=id)
    else: #idが無いとき（新規の時）
        #Memberを作成
        member = Member()

    #POSTの時（新規であれ編集であれ登録ボタンが押されたとき）
    if request.method == 'POST':
        #フォームを生成
        form = MemberForm(request.POST, instance=member)
        if form.is_valid(): #バリデーションがOKなら保存
            member = form.save(commit=False)
            member.save()
            return redirect('crud:index')
    else: #GETの時（フォームを生成）
        form = MemberForm(instance=member)

    #新規・編集画面を表示
    return render(request, 'members/edit.html', dict(form=form, id=id))

def delete(request, id):
    # return HttpResponse("削除")
    member = get_object_or_404(Member, pk=id)
    member.delete()
    return redirect('crud:index')

#詳細
def detail(request, id=id):
    member = get_object_or_404(Member, pk=id)
    return render(request, 'members/detail.html', {'member':member})