from django.shortcuts import render
from .models import Hotel, ReviewsHotel, CommentHotel
from django.core.paginator import Paginator
from .forms import CommentFormHotel
from django.http import HttpResponseRedirect

# Create your views here.
#def noidungkhachsan(request):
#    return render(request,'noidungkhachsan/noidungkhachsan.html')


def noidungkhachsan(request, id):
    khachsan = Hotel.objects.get(hotel_id=id)
    views = ReviewsHotel.objects.filter(hotel_id=id)
    paginator = Paginator(views, 5)
    page_number = request.GET.get('page')
    views = paginator.get_page(page_number)
    cmt = CommentHotel.objects.all()
    form = CommentFormHotel()
    if request.method == 'POST':
        form = CommentFormHotel(request.POST, author1=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    print(khachsan)
    context = {"Hotel": khachsan, "views":views, "form":form, "cmt":cmt}
    return render(request, 'noidungkhachsan/noidungkhachsan.html', context)