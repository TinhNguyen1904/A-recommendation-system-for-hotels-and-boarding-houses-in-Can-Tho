from django.urls import path
from .import views
from .views import home, search

app_name = 'NhaTroLogoutMemberUser'
urlpatterns = [
    path('', home.as_view(), name='home'),
    path('logout/', views.logoutUser, name='logoutUser'),
    #path('test/', home1.as_view(), name='test'),
    path('parameter/', views.search),
    path('parameter1/', views.search1),
]