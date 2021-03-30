# -*- coding: utf-8 -*-
# @File  : detailForm.py
# @Author: A35_Zhou
# @Date  : 2021/3/29
# @Software: PyCharm
from django import forms


class DetailForm(forms.Form):
    """
    使用django中的form组件生成个人信息界面form表单，并对用户输入内容校验
    """
    realname = forms.CharField(label='真实姓名',
                               max_length=16,
                               required=False,
                               error_messages={
                                   'max_length': '用户名最大8位'
                               },
                               widget=forms.TextInput(attrs={'class': 'form-control'})
                               )
    gender = forms.ChoiceField(label='性别',
                               required=False,
                               choices=((0, '隐藏'), (1, '男'), (2, '女')),
                               widget=forms.Select(attrs={'class': 'form-control'})
                               )
    idCard = forms.IntegerField(label='身份证号',
                                required=False,
                                widget=forms.NumberInput(attrs={'class': 'form-control'})
                                )
    cardCopy = forms.FileField(label='身份证复印件',
                               required=False,
                               widget=forms.FileInput()
                               )

    def clean_idCard(self):
        """
        使用局部hook校验用户身份证号是否正确
        """
        idCard = self.cleaned_data.get('idCard')
        if idCard is not None:
            if not len(str(idCard)) == 18:
                self.add_error('idCard', '身份证号为18位')
        return idCard
