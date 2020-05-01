from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from rest_framework import routers

#imports das views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]
