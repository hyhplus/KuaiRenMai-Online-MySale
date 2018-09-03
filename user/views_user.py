from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def test(request):
    return HttpResponse("用户个人设置和账号设置的逻辑层")

#账户设置
def account(request):
    return render(request, 'user/account.html')

#我的收藏
def colletion(requset):
    return render(requset,'user/collection.html')

#增加联系方式
def contact(requset):
    return render(requset,'user/contact.html')

#我的需求
def demand(request):
    return render(request,'user/demand.html')

#我的资料
def index(request):

    return render(request,'user/index.html')

#我的消息
def message(request):
    return render(request,'user/message.html')

#个人设置
def mybdhome(requset):
    return render(requset, 'user/mybdhome.html')

#退出登录
def out(request):
    return render(request,'user/out.html')

#钱袋
def walllet(request):
    return render(request,'user/wallet.html')

#发布合作信息
def release(request):
    return render(request,'user/release.html')