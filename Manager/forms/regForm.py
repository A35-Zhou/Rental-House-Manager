# -*- coding: utf-8 -*-
# @File  : regForm.py
# @Author: A35_Zhou
# @Date  : 2021/3/25
# @Software: PyCharm
from django import forms
from Manager import models


class RegForm(forms.Form):
    """
    使用django中的form组件生成注册界面form表单，并对用户输入内容校验
    """
    username = forms.CharField(label='用户名',
                               min_length=3,
                               max_length=8,
                               error_messages={
                                   'required': '用户名不能为空',
                                   'min_length': '用户名最少3位',
                                   'max_length': '用户名最大8位'
                               },
                               widget=forms.TextInput(attrs={'class': 'form-control'})
                               )
    email = forms.EmailField(label='邮箱',
                             required=False,
                             error_messages={
                                 'required': '邮箱不能为空',
                                 'invalid': '邮箱格式不正确'
                             },
                             widget=forms.EmailInput(attrs={'class': 'form-control'})
                             )
    password = forms.CharField(label='密码',
                               min_length=5,
                               max_length=16,
                               error_messages={
                                   'required': '密码不能为空',
                                   'min_length': '密码最少5位',
                                   'max_length': '密码最大16位'
                               },
                               widget=forms.PasswordInput(attrs={'class': 'form-control'})
                               )
    repassword = forms.CharField(label='确认密码',
                                 min_length=5,
                                 max_length=16,
                                 error_messages={
                                     'required': '确认密码不能为空',
                                     'min_length': '确认密码最少5位',
                                     'max_length': '确认密码最大16位'
                                 },
                                 widget=forms.PasswordInput(attrs={'class': 'form-control'})
                                 )

    def clean_username(self):
        """
        使用局部hook校验用户名是否存在
        """
        username = self.cleaned_data.get('username')
        is_exist = models.User.objects.filter(username=username)
        if is_exist:
            self.add_error('username', '用户名已存在')
        return username

    def clean(self):
        """
        使用全局hook校验用户密码输入是否一致
        """
        password = self.cleaned_data.get('password')
        repassword = self.cleaned_data.get('repassword')
        if not password == repassword:
            self.add_error('repassword', '密码输入不一致')
        return self.cleaned_data
