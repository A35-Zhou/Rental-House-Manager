from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from Manager import models
from iframe_api.forms.accountForm import AccountForm
from iframe_api.forms.detailForm import DetailForm


# Create your views here.
class Account(View):
    """
    处理用户帐号相关请求
    """

    def get(self, request):
        """
        处理用户帐号相关请求
        :param request: django路由响应默认携带request对象
        :return: 返回用户帐号管理界面
        """
        accountInfo = {
            'username': request.user.username,
            'email': request.user.email,
            'phone': request.user.phone,
            'wechat': request.user.wechat,
        }
        accountForm = AccountForm(accountInfo)
        return render(request, 'usermgr/account.html', locals())

    def post(self, request):
        """
        处理用户帐号相关请求
        :param request: django路由响应默认携带request对象
        :return: 返回帐号处理结果
        """
        if request.is_ajax():
            resultData = {'ret': None}
            accountForm = AccountForm(request.POST)
            if accountForm.is_valid():
                vaildData = accountForm.cleaned_data
                if not vaildData.get('username'):
                    vaildData.pop('username')
                    self.database_update(request, vaildData, resultData)
            elif request.POST.get('username') == request.user.username:
                vaildData = accountForm.cleaned_data
                self.database_update(request, vaildData, resultData)
            else:
                resultData['ret'] = 0
                resultData['msg'] = accountForm.errors
            return JsonResponse(resultData)

    def database_update(self, request, vaildData, resultData):
        """
        数据库操作
        :param request: django路由响应默认携带request对象
        :param vaildData: 操作数据
        :param resultData: 返回前端数据
        :return:
        """
        try:
            models.User.objects.filter(username=request.user.username).update(**vaildData)
        except Exception as e:
            resultData['ret'] = -1
            resultData['msg'] = f'{e}\n错误：后端数据库操作失败\n请联系管理员:\n'
            for superuser in models.User.objects.filter(is_superuser=1):
                resultData['msg'] += superuser.email
        else:
            resultData['ret'] = 1
        return resultData


class UserDetail(View):
    """
    处理用户信息相关请求
    """

    def get(self, request):
        """
        处理用户信息相关请求
        :param request: django路由响应默认携带request对象
        :return: 返回用户信息处理页面
        """
        userDetail = {
            'realname': request.user.detail.realname,
            'idCard': request.user.detail.idCard,
            'gender': request.user.detail.gender,
        }
        detailForm = DetailForm(userDetail)
        return render(request, 'usermgr/userdetail.html', locals())

    def post(self, request):
        """
        处理用户信息相关请求
        :param request: django路由响应默认携带request对象
        :return: 返回用户信息处理结果
        """
        if request.is_ajax():
            resultData = {'ret': None}
            detailForm = DetailForm(request.POST)
            if detailForm.is_valid():
                vaildData = detailForm.cleaned_data
                cardCopy = request.FILES.get('cardCopy')
                print(cardCopy)
                if cardCopy:
                    vaildData['cardCopy'] = cardCopy
                self.database_update(request, vaildData, resultData)
            else:
                resultData['ret'] = 0
                resultData['msg'] = detailForm.errors
            return JsonResponse(resultData)

    def database_update(self, request, vaildData, resultData):
        """
        数据库操作
        :param request: django路由响应默认携带request对象
        :param vaildData: 操作数据
        :param resultData: 返回前端数据
        :return:
        """
        try:
            models.UserDetail.objects.filter(id=request.user.detail.id).update(**vaildData)
        except Exception as e:
            resultData['ret'] = -1
            resultData['msg'] = f'{e}\n错误：后端数据库操作失败\n请联系管理员:\n'
            for superuser in models.User.objects.filter(is_superuser=1):
                resultData['msg'] += superuser.email
        else:
            resultData['ret'] = 1
        return resultData


class Home(View):
    """
    返回主页iframe内容
    """

    def get(self, request):
        """
        处理用户管理相关请求
        :param request: django路由响应默认携带request对象
        :return: 返回用户管理主页
        """
        houseInfo = models.HouseInfo.objects.all()[0]
        return render(request, 'usermgr/home.html', locals())
