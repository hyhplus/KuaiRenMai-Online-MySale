from django.http import HttpResponse
from django.shortcuts import render
from user.models import Publish


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