from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    phone = models.BigIntegerField(verbose_name='手机号', null=True, blank=True)
    wechat = models.CharField(verbose_name='微信号', max_length=32, null=True, blank=True)
    detail = models.OneToOneField(to='UserDetail', verbose_name='个人信息', on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey(to='Room', verbose_name='房间号', null=True, blank=True, on_delete=models.PROTECT)
    createTime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'


class UserDetail(models.Model):
    realname = models.CharField(verbose_name='真实姓名', max_length=8, null=True, blank=True)
    gender = models.SmallIntegerField(verbose_name='性别', choices=((0, '隐藏'), (1, '男'), (2, '女')),  # 0隐藏 1男 2女
                                      default=0)
    idCard = models.BigIntegerField(verbose_name='身份证号', null=True, blank=True)
    cardCopy = models.FileField(verbose_name='身份证复印件', upload_to='id_card', null=True, blank=True)

    def __str__(self):
        return self.realname

    class Meta:
        verbose_name = '用户个人信息'
        verbose_name_plural = '用户个人信息'


class HouseInfo(models.Model):
    houseName = models.CharField(verbose_name='公寓名称', max_length=8, default='默认公寓名')
    houseDesc = models.CharField(verbose_name='公寓简介', max_length=256, default='默认公寓简介')
    houseSlogan = models.CharField(verbose_name='公寓标语', max_length=16, default='默认标语')
    location = models.CharField(verbose_name='地址', max_length=32, default='默认地址')
    brand = models.FileField(verbose_name='公寓商标',
                             upload_to='HouseImg/brand',
                             default='HouseImg/brand/defaultBrand.png')
    houseImg = models.FileField(verbose_name='公寓照片',
                                upload_to='HouseImg',
                                default='HouseImg/defaultHouse.png')

    def __str__(self):
        return self.houseName

    class Meta:
        verbose_name = '公寓信息'
        verbose_name_plural = '公寓信息'


class Room(models.Model):
    roomId = models.IntegerField(verbose_name='房间号', primary_key=True)
    floor = models.IntegerField(verbose_name='楼层', default=0)
    state = models.SmallIntegerField(verbose_name='状态',
                                     choices=((0, '闲置中'), (1, '预定中'), (2, '使用中')),  # 0闲置中 1预定中 2使用中
                                     default=0)
    type = models.ForeignKey(to='RoomType', verbose_name='房型', on_delete=models.PROTECT, null=True, blank=True)
    roomDesc = models.CharField(verbose_name='房间描述', max_length=255, default='默认房间描述')
    roomImg = models.FileField(verbose_name='房间照片',
                               upload_to='RoomImg',
                               default='RoomImg/defaultRoom')

    def __str__(self):
        return str(self.roomId)

    class Meta:
        verbose_name = '房间信息'
        verbose_name_plural = '房间信息'


class RoomType(models.Model):
    typeName = models.CharField(verbose_name='房型名称', max_length=16, default='默认房型')
    typeImg = models.FileField(verbose_name='房型示例',
                               upload_to='TypeImg',
                               default='TypeImg/defaultType')
    area = models.FloatField(verbose_name='大致面积', default=0)
    edayRent = models.FloatField(verbose_name='预估租金/天', default=0)
    emonRent = models.FloatField(verbose_name='预估租金/月', default=0)
    eDeposit = models.FloatField(verbose_name='预估押金', default=0)
    TypeDesc = models.CharField(verbose_name='房间描述', max_length=255, default='默认房间描述')

    def __str__(self):
        return self.typeName

    class Meta:
        verbose_name = '房型信息'
        verbose_name_plural = '房型信息'


class Order(models.Model):
    orderId = models.AutoField(verbose_name='订单号', primary_key=True, auto_created=True)
    user = models.ForeignKey(to='User', verbose_name='用户', on_delete=models.PROTECT)
    room = models.ForeignKey(to='Room', verbose_name='房间号', on_delete=models.PROTECT)
    inTime = models.DateTimeField(verbose_name='入住时间')
    outTime = models.DateTimeField(verbose_name='离开时间')
    createTime = models.DateTimeField(verbose_name='订单创建时间', auto_now_add=True)
    ePay = models.FloatField(verbose_name='预付金额')
    payState = models.BooleanField(verbose_name='支付情况', choices=((True, '已支付'), (False, '未支付')), default=False)
    orderDesc = models.CharField(verbose_name='订单描述', max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.orderId)

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = '订单'


class Contract(models.Model):
    contractId = models.AutoField(verbose_name='合同号', primary_key=True, auto_created=True)
    user = models.ForeignKey(to='User', verbose_name='用户', on_delete=models.PROTECT)
    room = models.ForeignKey(to='Room', verbose_name='房间号', on_delete=models.PROTECT)
    inTime = models.DateTimeField(verbose_name='入住时间')
    outTime = models.DateTimeField(verbose_name='离开时间')
    createTime = models.DateTimeField(verbose_name='合同创建时间', auto_now_add=True)
    rPay = models.FloatField(verbose_name='实付金额')
    payState = models.BooleanField(verbose_name='支付情况', default=False)
    contract = models.TextField(verbose_name='合同内容', default='合同内容')
    signature = models.FileField(verbose_name='实体合同', upload_to='Contracts')

    def __str__(self):
        return str(self.contractId)

    class Meta:
        verbose_name = '合同'
        verbose_name_plural = '合同'
