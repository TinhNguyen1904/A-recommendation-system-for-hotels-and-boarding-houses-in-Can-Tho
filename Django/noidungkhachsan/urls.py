from django.urls import path
from .import views

urlpatterns = [
    #path('', views.noidungkhachsan),
    path('<int:id>', views.noidungkhachsan),
]