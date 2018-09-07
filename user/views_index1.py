from django.http import HttpResponse
from django.shortcuts import render
from mysale.user.models import Publish
from mysale.user.models import Sort

#coding=utf-8

# Create your views here.
def test(request):
    return HttpResponse("发布需求和回复需求的逻辑层")


def index(request):
    # pub = Publish.objects.all()
    #
    # for pu in pub:
    #     context = {'title':pu.title}
    return render(request, 'pub/index.html')



def publish(request):
    return render(request, 'pub/publish.html')


def publish_handler(request):
    title=request.POST.get('title')
    image=request.POST.get('image')
    tel=request.POST.get('tel')
    qq=request.POST.get('qq')
    wechat=request.POST.get('wechat')
    start_time=request.POST.get('start_time')
    end_time=request.POST.get('end_time')
    reward=request.POST.get('reward')
    is_top=request.POST.get('is_top')
    is_flush=request.POST.get('is_flush')
    detail=request.POST.get('detail')

    sort_1 = request.POST.get('sort_1')
    sort_2 = request.POST.get('sort_2')
    area=request.POST.get('area')
    sort=Sort()
    if is_top==None or is_top=="":
        is_top="False"
    if is_flush==None or is_flush=="":
        is_flush="False"
    if reward=="":
        reward=0


    #判断二级下拉分类
    if sort_1 == "1":
        if sort_2 == "0":
            sort.pet=1
        else: #sort_2 == 2
            sort.pet=2
    elif sort_1 == "2":
        if sort_2 == "0":
            sort.home=1
        elif sort_2 == "1":
            sort.home=2
        else: #sort_2 == 3
            sort.home=3
    elif sort_1 == "3":
        if sort_2 == "0":
            sort.market=1
        elif sort_2 == "1":
            sort.market=2
        elif sort_2 == "2":
            sort.market=3
        elif sort_2 == "3":
            sort.market=4
        elif sort_2 == "4":
            sort.market=5
        elif sort_2 == "5":
            sort.market=6
        else: #sort_2 == 7
            sort.home=7
    elif sort_1 == "4":
        if sort_2 == "0":
            sort.find=1
        elif sort_2 == "1":
            sort.find=2
        elif sort_2 == "2":
            sort.find=3
        else: #sort_2 == 4:
            sort.find=4
    elif sort_1 == "5":
        if sort_2 == "0":
            sort.connect=1
        elif sort_2 == "1":
            sort.connect=2
        else: #sort_2 == 3:
            sort.connect=3
    else: #sort_1 == 6:
        if sort_2 == "0":
            sort.live=1
        elif sort_2 == "1":
            sort.live=2
        elif sort_2 == "2":
            sort.live=3
        elif sort_2 == "3":
            sort.live=4

    #return HttpResponse(sort.pet)
    try:
        publish=Publish()
        publish.title=title
        publish.image=image
        publish.tel=tel
        publish.qq=qq
        publish.wechat=wechat
        publish.end_time=end_time
        publish.reward=reward
        publish.is_top=is_top
        publish.is_flush=is_flush
        publish.detail=detail
        sort.area=area
        publish.save()
        sort.save()
        return render(request, 'pub/index.html')
    except Exception as e:
        return render(request, 'pub/publish.html')