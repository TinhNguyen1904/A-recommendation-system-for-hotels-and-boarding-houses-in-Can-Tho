from django.urls import path
from .import views
app_name = 'MemberUser'
urlpatterns = [
    path('register/', views.dangnhapdangky.as_view(), name = 'registerUser'),
    path('login/', views.loginUser.as_view(), name = 'loginUser'),
]