from django.urls import path
from .import views
from .views import home, searchHotel
app_name = 'LogoutMemberUser'
urlpatterns = [
    path('', home.as_view(), name='home'),
    #path('', views.KhachSan),
    path('logout/', views.logoutUser, name='logoutUser'),
    #path('', views.privatePage, name = 'privatePage'),
    path('parameter/', views.searchHotel),
    path('parameter1/', views.searchHotel1),
]
