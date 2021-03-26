from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from Manager import models
from Manager.forms.regform import RegForm


# Create your views here.
class Register(View):
    """
    针对user/register/路由请求响应的视图类Register
    """

    def get(self, request):
        """
        针对get请求的响应
        :param request: django路由响应需携带request对象
        :return: 返回register.html
        """
        regForm = RegForm()
        return render(request, 'register.html', locals())

    def post(self, request):
        """
        针对post请求的响应
        :param request: django路由响应需携带request对象
        :return: 返回form表单校验结果 ret:1注册成功 0用户输入错误 -1数据库操作失败
        """
        resultData = {'ret': None}
        regForm = RegForm(request.POST)
        if regForm.is_valid():
            vaildData = regForm.cleaned_data
            vaildData.pop('repassword')
            try:
                models.User.objects.create_user(**vaildData)
            except:
                resultData['ret'] = -1
                resultData['msg'] = '错误：后端数据库操作失败\n请联系管理员:\n'
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
        :param request: django路由响应需携带request对象
        :return: 返回register.html
        """
        return render(request, 'login.html')

    def post(self, request):
        """
        针对post请求的响应
        :param request: django路由响应需携带request对象
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
