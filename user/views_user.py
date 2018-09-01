from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def test(request):
    return HttpResponse("用户个人设置和账号设置的逻辑层")