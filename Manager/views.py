from django.contrib import auth
# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse
from django.views import View

from Manager import models
from Manager.forms.regForm import RegForm
from Manager.forms.rspwdForm import RspwdForm


# Create your views here.
class Register(View):
    """
    针对user/register/路由请求响应的视图类Register
    """

    def get(self, request):
        """
        针对get请求的响应
        :param request: django路由响应默认携带request对象
        :return: 返回register.html
        """
        regForm = RegForm()
        return render(request, 'register.html', locals())

    def post(self, request):
        """
        针对post请求的响应
        :param request: django路由响应默认携带request对象
        :return: 返回form表单校验结果 ret:1注册成功 0用户输入错误 -1数据库操作失败
        """
        if request.is_ajax():
            resultData = {'ret': None}
            regForm = RegForm(request.POST)
            if regForm.is_valid():
                vaildData = regForm.cleaned_data
                vaildData.pop('repassword')
                try:
                    models.User.objects.create_user(**vaildData)
                except Exception as e:
                    resultData['ret'] = -1
                    resultData['msg'] = f'{e}\n错误：后端数据库操作失败\n请联系管理员:\n'
                    for superuser in models.User.objects.filter(is_superuser=1):
                        resultData['msg'] += superuser.email
                else:
                    resultData['ret'] = 1
                    resultData['url'] = 'user/login/'
            else:
                resultData['ret'] = 0
                resultData['msg'] = regForm.errors
            return JsonResponse(resultData)


class Login(View):
    """
    针对user/login/路由请求响应的视图类Login
    """

    def get(self, request):
        """
        针对get请求的响应
        :param request: django路由响应默认携带request对象
        :return: 返回register.html
        """
        return render(request, 'login.html')

    def post(self, request):
        """
        针对post请求的响应
        :param request: django路由响应默认携带request对象
        :return: 返回登录校验结果 ret:1登录成功 0用户名或密码错误
        """
        resultData = {'ret': None}
        user_is_exsit = auth.authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user_is_exsit:
            auth.login(request, user_is_exsit)
            resultData['ret'] = 1
            resultData['url'] = '/'
        else:
            resultData['ret'] = 0
            resultData['msg'] = '用户名或者密码错误'
        return JsonResponse(resultData)


class MainPage(View):
    """
    主页
    """

    def get(self, request):
        """
        返回主页html
        :param request: django路由响应默认携带request对象
        :return:返回mainpage.html渲染页面
        """
        rspwdForm = RspwdForm()
        houseInfo = models.HouseInfo.objects.all()[0]
        return render(request, 'mainpage.html', locals())


class ResetPassword(View):
    """
    修改密码相关操作
    """

    def post(self, request):
        """
        处理修改用户密码的请求
        :param request: django路由响应默认携带request对象
        :return:返回修改请求的结果
        """
        resultData = {'ret': None}
        if request.is_ajax():
            rspwdForm = RspwdForm(request.POST)
            if rspwdForm.is_valid():
                try:
                    request.user.set_password(request.POST.get('newpassword'))
                    request.user.save()
                except:
                    resultData['ret'] = -1
                    resultData['msg'] = '错误：后端数据库操作失败\n请联系管理员:\n'
                    for superuser in models.User.objects.filter(is_superuser=1):
                        resultData['msg'] += superuser.email
                else:
                    resultData['ret'] = 1
                    resultData['url'] = reverse('user:login')
            else:
                resultData['ret'] = 0
                resultData['msg'] = rspwdForm.errors
        return JsonResponse(resultData)


class Logout(View):
    """
    处理用户退出登录的请求
    """

    def get(self, request):
        """
        处理用户退出登录相关请求
        :param request: django路由响应默认携带request对象
        :return: 回到主页
        """
        auth.logout(request)
        return redirect('/')


class UserMgrBase(View):
    """
    处理用户管理相关请求
    """

    def get(self, request):
        """
        处理用户管理相关请求
        :param request: django路由响应默认携带request对象
        :return: 返回用户管理主页
        """
        houseInfo = models.HouseInfo.objects.all()[0]
        return render(request, 'usermgr/base.html', locals())
