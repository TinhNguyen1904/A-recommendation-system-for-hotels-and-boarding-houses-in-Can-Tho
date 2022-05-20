from django.shortcuts import render, HttpResponse
from django.views.generic import ListView,FormView
from .models import Room, Booking
from .forms import AvailabilityForm
from home.booking_functions.availability import check_avallabitily
from noidungkhachsan.models import Hotel
# Create your views here.
def index (request):
    return render(request, 'home/index.html')

# def datphong(request, id):
#     khachsan = Hotel.objects.get(hotel_id=id)
#     print(khachsan)
#     context = {"Hotel": khachsan}
#     return render(request, 'home/123.html', context)

# class homebook(FormView):
#     def get(self, request):
#         obj1 = Hotel.objects.all()
#         return render(request, 'home/123.html', {'obj1': obj1})

class RoomList(ListView):
    model=Room

class BookingList(ListView):
    model=Booking

class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = 'home/123.html'

    def form_valid(self, form):
        #obj1 = Hotel.objects.get(hotel_id=id)
        #return render(self.request, 'home/123.html', {'obj1': obj1})
        data = form.cleaned_data
        room_list = Room.objects.filter(category=data['room_category'])
        available_room = []
        for room in room_list:
            if check_avallabitily(room, data['check_in'], data['check_out']):
                available_room.append(room)

        if len(available_room)>0:
            room = available_room[0]
            booking = Booking.objects.create(
                user=self.request.user,
                room=room,
                check_in=data['check_in'],
                check_out=data['check_out']
            )
            booking.save()
            return render(self.request, 'home/congratulation.html')
        else:
            return render(self.request, 'home/error.html')

