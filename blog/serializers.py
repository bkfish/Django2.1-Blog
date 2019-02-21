from rest_framework import serializers
from .models import Blog


class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog  # 指定的模型类
        fields = ('title', 'blog_type', 'content', 'author')  # 需要序列化的属性