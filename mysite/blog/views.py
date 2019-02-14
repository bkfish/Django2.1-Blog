from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .models import Blog, BlogType
from .serializers import BlogSerializers, BlogTypeSerializers


# Create your views here.
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-pk')
    serializer_class = BlogSerializers


class BlogTypeViewSet(viewsets.ModelViewSet):
    queryset = BlogType.objects.all().order_by('-pk')
    serializer_class = BlogTypeSerializers



