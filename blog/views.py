from django.shortcuts import render, render_to_response, get_object_or_404
from rest_framework import viewsets
from .models import Blog, BlogType
from .serializers import BlogSerializers, BlogTypeSerializers
from django.core.paginator import Paginator


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
    page_num = request.GET.get('page', 1)  # 获取页码参数
    blogs_all_list = Blog.objects.all()
    paginator = Paginator(blogs_all_list, 10)  # 每10页分页
    page_of_blogs = paginator.get_page(page_num)  # 一旦出错就为1
    currentr_page_num=page_of_blogs.number #当前页
    page_range=list(range(max(currentr_page_num-2,1),currentr_page_num)) + list(range(currentr_page_num,min(currentr_page_num+2,paginator.num_pages)+1))
    # 加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)
    context = {'page_of_blogs': page_of_blogs, 'blog_types': BlogType.objects.all(),'page_range':page_range} # page_of_blogs带内容和页数
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
