from django import forms
"""
该表单用于对用户进行验证
PasswordInput微件显示其HTML input元素，同时包含type="password"属性
以使浏览器可将其视作密码输入
"""
class LoginForm(forms.Form):
    username=forms.CharField()
    password =forms.CharField(widget=forms.PasswordInput)

