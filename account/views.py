from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm,UserRegistrationForm
# Create your views here.
from django.contrib.auth.decorators import login_required

def user_login(request):
    """
    当用户输入完账号密码之后，通过按钮提交实际是向网站发送了一个POST请求
    于是将数据存放在了form中，通过LoginForm来实例化包含数据的表单那么request.POST实则是forms的一个子类
    然后检测form是否有效（用户是否输入完整），若是有效的
    那么通过authenticate（）函数来根据数据库中存在的用户进行验证，关注它的参数,传入该表单的请求，
    以及表单中的用户名和密码,验证成功则返回User对象,对象验证成功之后需要检测对象是否处于活动状态
    如果账户处于活动状态则登录网站（没有被拉黑？）
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()  # 当user_login通过GET方式时调用这里 实例化新的登录表单，并将其显示模板中
    return render(request, 'account/login.html', {'form': form})
@login_required
def dashboard(request):
    return render(request,'account/dashboard.html',{'section':'dashboard'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            #创建一个新的user对象但是并没有存储它
            new_user = user_form.save(commit=False)
            #设置用户密码
            new_user.set_password(user_form.cleaned_data['password'])
            #保存对象
            new_user.save()
            return render(request,'account/register_done.html',{'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,'account/register.html',{'user_form':user_form})






