from django import forms
from .models import Image
from django.core.files.base import ContentFile
from django.utils.text import slugify
import urllib

class ImageCreateForm(forms.ModelForm):
    """
    用户不会在该表单中直接输入图像URL。将通过JavaScript从外部站点中选择一幅图像
    对应表单将作为参数接受其URL。
    HiddenInput 基于<input type="hidden>属性  因为我们并不需要该字段对用户可见
    """
    class Meta:
        model = Image
        fields = ('title','url','description')
        widgets = {'url': forms.HiddenInput,}

    def clean_url(self):
        """
        检测提供的图像URL是否以.jpg或者.jrpg结尾，且仅支持JPEG文件
        :return:
        """
        url  = self.cleaned_data['url']
        valid_extensions = ['jpg','jpeg']
        #rsplit 选择以'.'作为分割符，分割一次 产生一个长度为2的列表[1]访问了列表的最后一个元素
        #即URL的后缀并变成小写lower()
        extension = url.rsplit('.',1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError("The given URL does not match valid image extensions.")
        return url

    def save(self,force_insert = False,
                  force_update = False,
                 commit = True):
        """
        覆写ModelForm提供的save()函数将当前模型实例保存至数据库中并返回该对象
        先通过调用ModleForm的save()方法并且commit为False 创建了新的image实例
        通过cleaned_data目录获得url，然后给通过image的标题和原始文件的后缀名进行组合形成新的图像名称
        使用Python urllib网络模块下载图像，并且将文件保存在项目当中
        :param force_insert:
        :param force_update:
        :param commit:
        :return:
        """
        image = super(ImageCreateForm,self).save(commit=False)
        image_url = self.cleaned_data['url']
        image_name = '{}.{}'.format(slugify(image.title),image_url.rsplit('.',1)[1].lower())

        #下载图片通过给定的url
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}

        response = urllib.request.urlopen(urllib.request.Request(image_url, headers=headers))
        image.image.save(image_name,ContentFile(response.read()),save=False)
        if commit:
            image.save()
        return image
#https://timgsa.baidu.com/timg?image
#https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1566478082627&di=471c252b993709d7ae294548a5489619
# &imgtype=0&src=http%3A%2F%2Fu.candou.com%2Fs%2F500%2F2018%2F1022%2F1540197714865.jpeg