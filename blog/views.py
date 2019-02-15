from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .models import Blog, BlogType
from .serializers import BlogSerializers, BlogTypeSerializers


# 提供API
# Create your views here.
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-pk')
    serializer_class = BlogSerializers


class BlogTypeViewSet(viewsets.ModelViewSet):
    queryset = BlogType.objects.all().order_by('-pk')
    serializer_class = BlogTypeSerializers


# 使用django自带模板
def blog_list(request):
    context = {'blogs': Blog.objects.all(), 'blog_types': BlogType.objects.all()}
    return render_to_response('blog/blog_list.html', context)


def blog_detail(request, blog_pk):
    context = {'blog': get_object_or_404(Blog, pk=blog_pk)}
    return render_to_response('blog/blog_detail.html', context)


def blogs_with_type(request, blog_type_pk):
    context = {}
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    context['blog_type'] = blog_type
    context['blog_types'] = BlogType.objects.all()
    return render_to_response('blog/blogs_with_type.html', context)
