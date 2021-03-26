from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    phone = models.BigIntegerField(verbose_name='手机号', null=True)
    wechat = models.CharField(verbose_name='微信号', max_length=32, null=True)
    detail = models.OneToOneField(to='UserDetail', on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(to='Room', null=True, on_delete=models.PROTECT)
    createTime = models.DateTimeField(auto_now_add=True)


class UserDetail(models.Model):
    realname = models.BigIntegerField(verbose_name='真实姓名', null=True)
    idCard = models.BigIntegerField(verbose_name='身份证号', null=True)
    cardCopy = models.FileField(verbose_name='身份证复印件', upload_to='id_card', null=True)


class HouseInfo(models.Model):
    houseName = models.CharField(verbose_name='公寓名称', max_length=16, null=True)
    houseDesc = models.CharField(verbose_name='公寓简介', max_length=256, null=True)
    location = models.CharField(verbose_name='地址', max_length=32, null=True)
    houseImg = models.FileField(verbose_name='公寓照片', upload_to='Img/HouseImg', null=True)


class Room(models.Model):
    roomId = models.IntegerField(verbose_name='房间号', primary_key=True)
    floor = models.IntegerField(verbose_name='楼层', null=True)
    state = models.IntegerField(verbose_name='状态', default=0)  # 0闲置 1预定 2使用中
    type = models.ForeignKey(to='RoomType', on_delete=models.PROTECT, null=True)
    roomDesc = models.CharField(verbose_name='房间描述', max_length=255, null=True)
    roomImg = models.FileField(verbose_name='房间照片', upload_to='Img/RoomImg', null=True)


class RoomType(models.Model):
    typeName = models.CharField(verbose_name='房型名称', max_length=16, null=True)
    typeImg = models.FileField(verbose_name='房型示例', upload_to='Img/RoomImg', null=True)
    area = models.FloatField(verbose_name='大致面积', null=True)
    edayRent = models.FloatField(verbose_name='预估租金/天', null=True)
    emonRent = models.FloatField(verbose_name='预估租金/月', null=True)
    eDeposit = models.FloatField(verbose_name='预估押金', null=True)
    TypeDesc = models.CharField(verbose_name='房间描述', max_length=255, null=True)


class Order(models.Model):
    orderId = models.AutoField(verbose_name='订单号', primary_key=True, auto_created=True)
    user = models.ForeignKey(to='User', on_delete=models.PROTECT)
    room = models.ForeignKey(to='Room', on_delete=models.PROTECT)
    inTime = models.DateTimeField(verbose_name='入住时间')
    outTime = models.DateTimeField(verbose_name='离开时间')
    createTime = models.DateTimeField(verbose_name='订单创建时间', auto_now_add=True)
    ePay = models.FloatField(verbose_name='预付金额')
    payState = models.BooleanField(verbose_name='支付情况', default=False)
    orderDesc = models.CharField(verbose_name='订单描述', max_length=255, null=True)


class Contract(models.Model):
    contractId = models.AutoField(verbose_name='合同号', primary_key=True, auto_created=True)
    user = models.ForeignKey(to='User', on_delete=models.PROTECT)
    room = models.ForeignKey(to='Room', on_delete=models.PROTECT)
    inTime = models.DateTimeField(verbose_name='入住时间')
    outTime = models.DateTimeField(verbose_name='离开时间')
    createTime = models.DateTimeField(verbose_name='合同创建时间', auto_now_add=True)
    rPay = models.FloatField(verbose_name='实付金额')
    payState = models.BooleanField(verbose_name='支付情况', default=False)
    contract = models.TextField(verbose_name='合同内容')
    signature = models.FileField(verbose_name='实体合同', upload_to='Contracts')