from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import ImageCreateForm
from .models import Image
@login_required
def image_create(request):
    if request.method == 'POST':
        #form提交
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            #将当前用户赋值给这个item的user字段
            new_item.user = request.user
            new_item.save()
            messages.success(request,'Image added successfully')
            return redirect(new_item.get_absolute_url())
    else:
        form =  ImageCreateForm(data=request.GET)

    return render(request,'images/image/create.html',{'section':'images',
                                                     'form':form})
#http://127.0.0.1:8000/images/create/?title=%20this%20is%20a%20game&url=https://img.lolttaaas.com/im/201806/20186221781291997.jpg
def image_detail(request,id,slug):
    image = get_object_or_404(Image,id = id ,slug = slug)
    return  render(request,'images/image/detail.html',
                   {'section':'image',
                    'image':image})
