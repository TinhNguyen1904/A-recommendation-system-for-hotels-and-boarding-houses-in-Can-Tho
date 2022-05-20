from django.urls import path
from .import views

urlpatterns = [
    # path('', views.noidungnhatro),
    path('<int:id>', views.noidungnhatro),
]