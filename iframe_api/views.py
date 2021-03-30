from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from Manager import models
from iframe_api.forms.orderForm import OrderForm
from iframe_api.forms.accountForm import AccountForm
from iframe_api.forms.detailForm import DetailForm


# Create your views here.
class Home(View):
    """
    返回主页iframe内容
    """

    def get(self, request):
        """
        处理用户管理相关请求
        :param request: django路由响应默认携带request对象
        :return: 返回主页iframe
        """
        houseInfo = models.HouseInfo.objects.all()[0]
        return render(request, 'usermgr/home.html', locals())


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
        return render(request, 'usermgr/user/account.html', locals())

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
        :param resultData: 前端结果
        :return: 返回前端结果
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
        try:
            userDetail = {
                'realname': request.user.detail.realname,
                'idCard': request.user.detail.idCard,
                'gender': request.user.detail.gender,
            }
        except AttributeError as e:
            detailForm = DetailForm()
        else:
            detailForm = DetailForm(userDetail)
        return render(request, 'usermgr/user/userdetail.html', locals())

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
        :param resultData: 前端结果
        :return: 返回前端结果
        """
        try:
            try:
                detail_id = request.user.detail.id
            except AttributeError as e:
                user_id = request.user.id
                userDetail = models.UserDetail.objects.create(**vaildData)
                userDetail.save()
                models.User.objects.filter(id=user_id).update(detail=userDetail.id)
            else:
                models.UserDetail.objects.filter(id=detail_id).update(**vaildData)
        except Exception as e:
            resultData['ret'] = -1
            resultData['msg'] = f'{e}\n错误：后端数据库操作失败\n请联系管理员:\n'
            for superuser in models.User.objects.filter(is_superuser=1):
                resultData['msg'] += superuser.email
        else:
            resultData['ret'] = 1
        return resultData


class HouseInfo(View):
    """
    返回公寓信息
    """

    def get(self, request):
        """
        处理公寓信息相关请求
        :param request: django路由响应默认携带request对象
        :return: 返回公寓信息
        """
        houseInfo = models.HouseInfo.objects.first()
        return render(request, 'usermgr/house/houseinfo.html', locals())


class RoomInfo(View):
    """
    返回房间信息
    """

    def get(self, request):
        """
        处理房间信息相关请求
        :param request: django路由响应默认携带request对象
        :return: 返回房间信息
        """
        roomInfo = models.Room.objects.all()
        return render(request, 'usermgr/house/roominfo.html', locals())


class TypeInfo(View):
    """
    返回房型信息
    """

    def get(self, request):
        """
        处理房型信息相关请求
        :param request: django路由响应默认携带request对象
        :return: 返回房型信息
        """
        typeInfo = models.RoomType.objects.all()
        return render(request, 'usermgr/house/typeinfo.html', locals())


class NewOrder(View):
    """
    处理新预约订单
    """

    def get(self, request):
        """
        获取新预约订单页面
        :param request: django路由响应默认携带request对象
        :return: 返回新预约订单页面
        """
        room_list = []
        rooms = models.Room.objects.all()
        for room in rooms:
            if room.state == 0:
                room_list.append(room.roomId)
        return render(request, 'usermgr/order/neworder.html', locals())

    def post(self, request):
        """
        获取新预约数据
        :param request: django路由响应默认携带request对象
        :return: 返回预约结果
        """
        resultData = {'ret': None}
        if request.is_ajax():
            room = models.Room.objects.filter(roomId=request.POST.get('room')).first()
            if not room.state:
                orderForm = OrderForm(request.POST)
                if orderForm.is_valid():
                    days = (orderForm.cleaned_data.get('outTime') - orderForm.cleaned_data.get('inTime')).days
                    if not int(request.POST.get('method')):
                        ePay = days * room.type.edayRent + room.type.eDeposit
                    else:
                        ePay = -(- days // 10) * room.type.emonRent + room.type.eDeposit
                    resultData['ePay'] = ePay
                    vaildData = orderForm.cleaned_data
                    vaildData['ePay'] = ePay
                    vaildData['user_id'] = request.user.id
                    vaildData['room_id'] = request.POST.get('room')
                    vaildData['orderDesc'] = request.POST.get('orderDesc')
                    self.database_update(vaildData, resultData)
                    models.Room.objects.filter(roomId=request.POST.get('room')).update(state=1)
                else:
                    resultData['ret'] = 0
                    resultData['msg'] = orderForm.errors
        return JsonResponse(resultData)

    def database_update(self, vaildData, resultData):
        """
        数据库操作
        :param request: django路由响应默认携带request对象
        :param vaildData: 操作数据
        :param resultData: 前端结果
        :return: 返回前端结果
        """
        try:
            models.Order.objects.create(**vaildData)
        except Exception as e:
            resultData['ret'] = -1
            resultData['msg'] = f'{e}\n错误：后端数据库操作失败\n请联系管理员:\n'
            for superuser in models.User.objects.filter(is_superuser=1):
                resultData['msg'] += superuser.email
        else:
            resultData['ret'] = 1
            resultData['url'] = reverse('iframe_api:userorder')
        return resultData


class UserOrder(View):
    """
    返回用户订单信息
    """

    def get(self, request):
        """
        处理用户订单信息相关请求
        :param request: django路由响应默认携带request对象
        :return: 返回用户订单信息
        """

        return render(request, 'usermgr/order/userorder.html', locals())
