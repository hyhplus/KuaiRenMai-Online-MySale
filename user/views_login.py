from hashlib import md5

from django.http import HttpResponse
from django.shortcuts import render, redirect, loader

from user.models import User



# Create your views here.
def test(request):
    return HttpResponse("登陆注册的逻辑层")


def register(request):
    return render(request, 'login/register.html')


def register_handler(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    copy_pwd = request.POST.get('copy_pwd')

    print(username)
    print(password)

    if password != copy_pwd:
        return redirect('/register/')
    else:
        u = User()
        if u.findName(username):

            md = md5()
            md.update(password.encode())
            pwd = md.hexdigest()
            u.create(username, pwd)
            print("u : %s",u)
        else:
            return render(request, 'login/register.html')
    return redirect('/login/')


def login(request):
    return render(request, 'login/login.html')


def login_handler(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    isChecked = request.POST.get('is_checked', '')

    if password == '':
        context = {'error' : '密码不能为空'}
        return render(request, 'login/login.html', context)

    u = User()
    if u.findName(username, password):
        request.session['user'] = username
        if isChecked == '' or 1==1:
        #if isChecked == 'on':
            context = {'s' : 1}
            content = loader.render_to_string('pub/1.html',context,request)
            hp = HttpResponse(content)
            hp.set_cookie('user', username)
            return hp

        return redirect('/login/')
    context = {'error' : '用户名或密码错误'}
    return render(request, 'login/login.html', context)

