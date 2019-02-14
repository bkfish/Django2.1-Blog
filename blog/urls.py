from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers
from blog import views
from .views import blog_list

route = routers.DefaultRouter()
route.register(r'blog', views.BlogViewSet)
route.register(r'blogType', views.BlogTypeViewSet)

urlpatterns = [
    path('api/', include(route.urls)),
    path('<int:blog_pk>', views.blog_detail, name="blog_detail"),
    path('type/<int:blog_type_pk>',views.blogs_with_type,name="blogs_with_type")
]
