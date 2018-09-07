from django.http import HttpResponse
from django.shortcuts import render
from mysale.user.models import User
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






def index(request):
    a_a=request.POST.get('a_a')
    a_b = request.POST.get('a_b')
    a_c = request.POST.get('a_c')
    b_a = request.POST.get('b_a')
    b_b = request.POST.get('b_b')
    b_c = request.POST.get('b_c')
    b_d = request.POST.get('b_d')
    c_a = request.POST.get('c_a')
    c_b = request.POST.get('c_b')
    c_c = request.POST.get('c_c')
    c_d = request.POST.get('c_d')
    c_e = request.POST.get('c_e')
    c_f = request.POST.get('c_f')
    c_g = request.POST.get('c_g')
    c_h = request.POST.get('c_h')
    d_a = request.POST.get('d_a')
    d_b = request.POST.get('d_b')
    d_c = request.POST.get('d_c')
    d_d = request.POST.get('d_d')
    d_e = request.POST.get('d_e')
    e_a = request.POST.get('e_a')
    e_b = request.POST.get('e_b')
    e_c = request.POST.get('e_c')
    e_d = request.POST.get('e_d')
    f_a = request.POST.get('f_a')
    f_b = request.POST.get('f_b')
    f_c = request.POST.get('f_c')
    f_d = request.POST.get('f_d')
    f_e = request.POST.get('f_e')
    g_a = request.POST.get('g_a')
    g_b = request.POST.get('g_b')
    g_c = request.POST.get('g_c')
    g_d = request.POST.get('g_d')
    g_e = request.POST.get('g_e')
    return HttpResponse(a_a)




    #return HttpResponse(sort.pet)
    # try:
    #     sort=Sort()
    #
    #     sort.area=area
    #     publish.save()
    #     sort.save()
    #     return render(request, 'pub/index.html')
    # except Exception as e:
    #     return render(request, 'pub/publish.html')