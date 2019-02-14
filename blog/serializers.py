from rest_framework import serializers
from .models import Blog, BlogType


class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog  # 指定的模型类
        fields = ('id', 'title', 'content', 'blog_type', 'author', 'created_time', 'last_updated_time')  # 需要序列化的属性


class BlogTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = BlogType
        fields = ('id', 'type_name')
