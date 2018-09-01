from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def test(request):
    return HttpResponse("登陆注册的逻辑层")