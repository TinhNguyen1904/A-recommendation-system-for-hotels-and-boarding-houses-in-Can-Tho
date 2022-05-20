from django.shortcuts import render
import numpy as np
from noidungkhachsan.models import Hotel
# Create your views here.
# def datphong(request):
#     return render(request, 'datphong/datphong.html')

def datphong(request, id):
    khachsan = Hotel.objects.get(hotel_id=id)
    print(khachsan)
    context = {"Hotel": khachsan}
    return render(request, 'datphong/datphong.html', context)

