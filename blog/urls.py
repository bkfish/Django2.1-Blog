from django.urls import path, include
from rest_framework import routers

from blog import views
# 定义路由地址
route = routers.DefaultRouter()

# 注册新的路由地址
route.register(r'blog', views.BlogViewSet)
# start with blog
urlpatterns = [
    # http://localhost:8000/blog/
    path('', views.blog_list, name='blog_list'),
    path('<int:blog_pk>', views.blog_detail, name="blog_detail"),
    path('type/<int:blog_type_pk>', views.blogs_with_type, name="blogs_with_type"),
    path('date/<int:year>/<int:month>', views.blogs_with_date, name="blogs_with_date"),
    path('api/',include(route.urls)),
]