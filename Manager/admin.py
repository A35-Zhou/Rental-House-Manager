from django.contrib import admin
from django.utils.translation import gettext_lazy

from Manager import models
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import ModelAdmin


# Register your models here.
# admin.site.register(models.User)
# admin.site.register(models.UserDetail)
# admin.site.register(models.Room)
# admin.site.register(models.RoomType)
# admin.site.register(models.Order)
# admin.site.register(models.HouseInfo)
# admin.site.register(models.Contract)
# houseInfo = models.HouseInfo.objects.all()[0]
# admin.site.site_header = f'{houseInfo.houseName}管理系统'
# admin.site.site_title = f'{houseInfo.houseName}后台管理系统'


# Model Admin
@admin.register(models.User)
class UserInfoAdmin(UserAdmin, ModelAdmin):
    list_display = ('id', 'username', 'detail', 'room', 'phone', 'wechat', 'createTime')
    list_per_page = 50
    ordering = ('id',)
    list_display_links = ('id', 'username', 'room', 'phone', 'createTime', 'detail')
    search_fields = ('id', 'username', 'room', 'phone', 'createTime', 'detail')


@admin.register(models.UserDetail)
class UserDetailAdmin(ModelAdmin):
    list_display = ('id', 'realname', 'gender', 'idCard')
    list_per_page = 50
    ordering = ('id',)
    list_display_links = ('id', 'realname', 'gender', 'idCard')
    search_fields = ('id', 'realname', 'gender', 'idCard')


@admin.register(models.Room)
class RoomAdmin(ModelAdmin):
    list_display = ('roomId', 'floor', 'state', 'type')
    list_per_page = 50
    ordering = ('roomId',)
    list_display_links = ('roomId', 'floor', 'state', 'type')
    search_fields = ('roomId', 'floor', 'state', 'type')


@admin.register(models.RoomType)
class RoomTypeAdmin(ModelAdmin):
    list_display = ('id', 'typeName', 'area', 'edayRent', 'emonRent', 'eDeposit')
    list_per_page = 50
    ordering = ('id',)
    list_display_links = ('id', 'typeName', 'area', 'edayRent', 'emonRent', 'eDeposit')
    search_fields = ('id', 'typeName', 'area', 'edayRent', 'emonRent', 'eDeposit')


@admin.register(models.HouseInfo)
class HouseInfoAdmin(ModelAdmin):
    list_display = ('id', 'houseName', 'location')
    list_per_page = 50
    ordering = ('id',)
    list_display_links = ('id', 'houseName', 'location')
    search_fields = ('id', 'houseName', 'location')


@admin.register(models.Order)
class OrderAdmin(ModelAdmin):
    list_display = ('orderId', 'user', 'room', 'inTime', 'outTime', 'ePay', 'payState', 'createTime')
    list_per_page = 50
    ordering = ('orderId',)
    list_display_links = ('orderId', 'user', 'room', 'inTime', 'outTime', 'ePay', 'payState', 'createTime')
    search_fields = ('orderId', 'user', 'room', 'inTime', 'outTime', 'ePay', 'payState', 'createTime')


@admin.register(models.Contract)
class ContractAdmin(ModelAdmin):
    list_display = ('contractId', 'user', 'room', 'inTime', 'outTime', 'rPay', 'payState', 'createTime')
    list_per_page = 50
    ordering = ('contractId',)
    list_display_links = ('contractId', 'user', 'room', 'inTime', 'outTime', 'rPay', 'payState', 'createTime')
    search_fields = ('contractId', 'user', 'room', 'inTime', 'outTime', 'rPay', 'payState', 'createTime')
