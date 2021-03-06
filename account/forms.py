from django import forms
from django.contrib.auth.models import  User
from .models import Profile
"""
该表单用于对用户进行验证
PasswordInput微件显示其HTML input元素，同时包含type="password"属性
以使浏览器可将其视作密码输入
"""
class LoginForm(forms.Form):
    username=forms.CharField()
    password =forms.CharField(widget=forms.PasswordInput)

#创建一个表单，用户可以在此输入用户名、真实姓名以及密码
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password',widget=forms.PasswordInput )

    class Meta:
        model = User
        fields = ('username','first_name','email')
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['password']
#UserEditForm允许用户编辑Django用户模型的属性
class UserEditForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ('first_name','last_name','email')
#使得用户编辑保存自定义Profile模型中的配置数据
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth','photo')
