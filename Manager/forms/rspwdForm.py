# -*- coding: utf-8 -*-
# @File  : rspwdForm.py
# @Author: A35_Zhou
# @Date  : 2021/3/27
# @Software: PyCharm
from django import forms


# from Manager import models


class RspwdForm(forms.Form):
    """
    使用django中的form组件生成密码修改界面form表单，并对用户输入内容校验
    """
    oldpassword = forms.CharField(label='原密码',
                                  error_messages={
                                      'required': '请输入原密码',
                                  },
                                  widget=forms.PasswordInput(attrs={'class': 'form-control'})
                                  )
    newpassword = forms.CharField(label='新密码',
                                  min_length=5,
                                  max_length=16,
                                  error_messages={
                                      'required': '请输入新密码',
                                      'min_length': '密码最少5位',
                                      'max_length': '密码最大16位'
                                  },
                                  widget=forms.PasswordInput(attrs={'class': 'form-control'})
                                  )
    repassword = forms.CharField(label='确认新密码',
                                 min_length=5,
                                 max_length=16,
                                 error_messages={
                                     'required': '请再次输入新密码',
                                     'min_length': '密码最少5位',
                                     'max_length': '密码最大16位'
                                 },
                                 widget=forms.PasswordInput(attrs={'class': 'form-control'})
                                 )

    def clean(self):
        """
        使用全局hook校验用户原新密码是否一样，新密码输入是否一致
        """
        oldpassword = self.cleaned_data.get('oldpassword')
        newpassword = self.cleaned_data.get('newpassword')
        if oldpassword == newpassword:
            self.add_error('newpassword', '新密码不能与原密码一致')
        else:
            repassword = self.cleaned_data.get('repassword')
            if not newpassword == repassword:
                self.add_error('repassword', '密码输入不一致')
        return self.cleaned_data
