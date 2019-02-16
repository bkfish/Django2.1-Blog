from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class BlogType(models.Model):
    type_name = models.CharField(max_length=20)

    def __str__(self):
        return self.type_name


class Blog(models.Model):
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)  # 删除不发生什么
    created_time = models.DateTimeField(auto_now_add=True)  # 创建时间
    last_updated_time = models.DateTimeField(auto_now=True)  # 最后更新时间

    def __str__(self):
        return "<Blog: %s>" % self.title

    class Meta:
        ordering=['-created_time']