# -*- coding: utf-8 -*-
# @File  : orderForm.py
# @Author: A35_Zhou
# @Date  : 2021/3/30
# @Software: PyCharm
from django import forms

from datetime import date


class OrderForm(forms.Form):
    """
    使用django中的form组件生成订单信息界面form表单，并对用户输入内容校验
    """
    inTime = forms.DateField(label='入住时间', error_messages={'required': '请选择入住日期'})
    outTime = forms.DateField(label='离开时间', error_messages={'required': '请选择离开日期'})

    def clean_inTime(self):
        """
        使用局部hook校验入住日期是否有效
        """
        inTime = self.cleaned_data.get('inTime')
        today = date.today()
        if inTime < today:
            self.add_error('inTime', '入住时间无效，不得晚于今天')
        return inTime

    def clean(self):
        """
        使用全局hook校验离开日期是否有效
        """
        inTime = self.cleaned_data.get('inTime')
        outTime = self.cleaned_data.get('outTime')
        if inTime is not None and outTime is not None:
            if outTime < inTime:
                self.add_error('outTime', '离开时间无效，不得早于入住时间')
        return self.cleaned_data
