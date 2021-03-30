# -*- coding: utf-8 -*-
# @File  : accountForm.py
# @Author: A35_Zhou
# @Date  : 2021/3/29
# @Software: PyCharm
from django import forms

from Manager import models


class AccountForm(forms.Form):
    """
    使用django中的form组件生成帐号信息界面form表单，并对用户输入内容校验
    """
    username = forms.CharField(label='用户名',
                               min_length=3,
                               max_length=8,
                               required=False,
                               error_messages={
                                   'min_length': '用户名最少3位',
                                   'max_length': '用户名最大8位'
                               },
                               widget=forms.TextInput(attrs={'class': 'form-control'})
                               )
    email = forms.EmailField(label='邮箱',
                             required=False,
                             error_messages={
                                 'invalid': '邮箱格式不正确'
                             },
                             widget=forms.EmailInput(attrs={'class': 'form-control'})
                             )
    phone = forms.IntegerField(label='手机号',
                               required=False,
                               widget=forms.NumberInput(attrs={'class': 'form-control'})
                               )
    wechat = forms.CharField(label='微信号',
                             min_length=6,
                             max_length=20,
                             required=False,
                             error_messages={
                                 'min_length': '微信号最少6位',
                                 'max_length': '微信号最多20位',
                             },
                             widget=forms.TextInput(attrs={'class': 'form-control'})
                             )

    def clean_username(self):
        """
        使用局部hook校验变更后是否为已存在用户名
        """
        username = self.cleaned_data.get('username')
        is_exist = models.User.objects.filter(username=username)
        if is_exist:
            self.add_error('username', '用户名已存在')
        return username

    def clean_phone(self):
        """
        使用局部hook校验用户手机号是否正确
        """
        phone = self.cleaned_data.get('phone')
        if not len(str(phone)) <= 11:
            self.add_error('phone', '手机号最多11位')
        return phone
