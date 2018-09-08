# from django.http import HttpResponse
# from django.shortcuts import render
# from user.models import Publish
# from user.models import Sort
# from user.models import User
#
# #coding=utf-8
#
# # Create your views here.
# def index1_handler(request):
#     context={}
#     context['top1s']=User.top1.last()
#     context['top2s']=User.top2.last()
#     context['qqnames'] = User.qqname.last()
#     context['logopics'] = User.logopic.last()
#     context['lunpic1s'] = User.lunpic1.last()
#     context['lunpic2s'] = User.lunpic2.last()
#     context['lastpics'] = User.lastpic.last()
#     return render(request, 'pub/index1.html', context)
#
# def upload(request):
#     top1 = request.POST.get('top1')
#     top2 = request.POST.get('top2')
#     qqname = request.POST.get('qqname')
#     logopic = request.POST.get('logopic')
#     lunpic1 = request.POST.get('lunpic1')
#     lunpic2 = request.POST.get('lunpic2')
#     lastpic = request.POST.get('lastpic')
#     try:
#         user=User()
#         user.top1=top1
#         user.top2=top2
#         user.qqname=qqname
#         user.logopic=logopic
#         user.lunpic1=lunpic1
#         user.lunpic2=lunpic2
#         user.lastpic=lastpic
#         user.save()
#         return render(request, 'pub/index1.html')
#     except Exception as e:
#         return render(request, 'pub/publish.html')
#
#
#
# def index1(request):
#     return render(request,'pub/index1.html')

