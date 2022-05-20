from django.urls import path
from .import views
from .views import RoomList, BookingList, BookingView

app_name='hotel'
urlpatterns = [
    path('', views.index),
    path('room_list/', RoomList.as_view(), name='RoomList'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('booking/<int:id>', BookingView.as_view())
    #path('booking/', homebook.as_view())
    #path('booking/<int:id>', views.datphong),
]