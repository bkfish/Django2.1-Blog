from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers
from blog import views

route = routers.DefaultRouter()
route.register(r'blog', views.BlogViewSet)
route.register(r'blogType', views.BlogTypeViewSet)

urlpatterns = [
    path('api/', include(route.urls)),
]
