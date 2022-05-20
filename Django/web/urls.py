"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('NhaTro/', include('NhaTro.urls')),
    path('KhachSan/', include('KhachSan.urls')),
    path('noidungnhatro/', include('noidungnhatro.urls')),
    path('noidungkhachsan/', include('noidungkhachsan.urls')),
    path('datphong/', include('datphong.urls')),
    path('', include('dangnhapdangky.urls')),
    #path('dangnhapdangky/', include('dangnhapdangky.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('search/', include('NhaTro.urls')),
    path('searchHotel/', include('KhachSan.urls')),
    path('search1/', include('NhaTro.urls')),
    path('searchHotel1/', include('KhachSan.urls')),
]