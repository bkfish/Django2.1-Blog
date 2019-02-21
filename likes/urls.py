from django.urls import path
from rest_framework import routers

from . import views
# 定义路由地址

urlpatterns = [
    path('like_change/', views.like_change, name='like_change')
]