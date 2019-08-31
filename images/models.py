from django.db import models
from django.shortcuts import reverse
from django.conf import settings
from django.utils.text import slugify
# Create your models here.

class Image(models.Model):
    #定义一个一对多的关系 用户可以发布多个图像，每副图像由单一用户发布
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='images_created',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    #slug定义的一个简单的标题，仅仅包含字母、数字、下划线构建SEO友好的URL
    slug=models.SlugField(max_length=200,blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y-%m-%d')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True,db_index=True)
    #添加一个字段，用来定义多对多的关系
    #某幅图感兴趣的用户、某个用户对多幅图感兴趣
    #Django通过两个模型的主键
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                       related_name='images_liked',
                                       blank=True)

    def __str__(self):
        return self.title

    #若模板为提供slug，则使用Django提供的slugfiy()函数针对给定的title标题自动生成图像slug，随后保存图像

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)

    #为对象提供规范URL的常见模式是在模型中定义get_absolute_url()方法
    def get_absolute_url(self):
        return reverse('images:detail',args=[self.id,self.slug])

