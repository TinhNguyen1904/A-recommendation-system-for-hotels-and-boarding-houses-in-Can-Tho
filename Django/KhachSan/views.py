from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@login_required(login_url='/login/')
def KhachSan(request):
    return render(request,'KhachSan/KhachSan.html')

def logoutUser(request):
    logout(request)
    return render(request, 'home/index.html')

#@login_required
#def privatePage(request):
#    return render(request, 'KhachSan/KhachSan.html')

####################
from django.shortcuts import render
from noidungkhachsan.models import Hotel
from django.views import View
from django.core.paginator import Paginator
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class home(View):
    def get(self, request):
        obj = Hotel.objects.all()
        obj1 = Hotel.objects.all()
        paginator = Paginator(obj, 5)
        page_number = request.GET.get('page')
        obj = paginator.get_page(page_number)
        return render(request, 'KhachSan/KhachSan.html', {'obj': obj, 'obj1': obj1})

@csrf_exempt
def searchHotel(request):
    if request.method=="POST":
        obj1 = Hotel.objects.all()
        hotel_location = request.POST.get('diadiemKS')
        title_rating = request.POST.get('danhgiaKS')
        hotel_price_2 = request.POST.get('giaKS')
        if hotel_location:
            tfidf = TfidfVectorizer()
            overview_matrix = tfidf.fit_transform(['diadiemKS'])
            overview_matrix.shape
            similarity_matrix = linear_kernel(overview_matrix, overview_matrix)
            similarity_matrix
            obj3 = Hotel.objects.filter(hotel_location=hotel_location)
            paginator = Paginator(obj3, 5)
            page_number = request.GET.get('page')
            obj3 = paginator.get_page(page_number)
            arrObject = []
            for item in obj3:
                print(item.hotel_location)
                arrObject.append(item)
            print(len(arrObject))
            return render(request, 'KhachSan/test.html', {'obj': arrObject, 'obj1': obj1})
        else:
            tfidf = TfidfVectorizer()
            overview_matrix = tfidf.fit_transform(['giaKS'])
            overview_matrix.shape
            similarity_matrix = linear_kernel(overview_matrix, overview_matrix)
            similarity_matrix
            obj3 = Hotel.objects.filter(hotel_price_2=hotel_price_2)
            paginator = Paginator(obj3, 5)
            page_number = request.GET.get('page')
            obj3 = paginator.get_page(page_number)
            arrObject = []
            for item in obj3:
                print(item.hotel_location)
                arrObject.append(item)
            print(len(arrObject))
            return render(request, 'KhachSan/test.html', {'obj': arrObject, 'obj1': obj1})
    else:
        obj4 = Hotel.objects.raw('select * from hotel')
        print(obj4)
        return render(request, 'KhachSan/KhachSan.html', {'obj3': obj4})

@csrf_exempt
def searchHotel1(request):
    if request.method=="POST":
        obj1 = Hotel.objects.all()
        title_rating = request.POST.get('danhgiaKS')
        bed_type = request.POST.get('loaiphong')
        if title_rating:
            tfidf = TfidfVectorizer()
            overview_matrix = tfidf.fit_transform(['danhgiakhachsan'])
            overview_matrix.shape
            similarity_matrix = linear_kernel(overview_matrix, overview_matrix)
            similarity_matrix
            obj3 = Hotel.objects.filter(title_rating=title_rating)
            paginator = Paginator(obj3, 5)
            page_number = request.GET.get('page')
            obj3 = paginator.get_page(page_number)
            arrObject = []
            for item in obj3:
                print(item.hotel_location)
                arrObject.append(item)
            print(len(arrObject))
            return render(request, 'KhachSan/test.html', {'obj': arrObject, 'obj1': obj1})
        else:
            tfidf = TfidfVectorizer()
            overview_matrix = tfidf.fit_transform(['loaiphong'])
            overview_matrix.shape
            similarity_matrix = linear_kernel(overview_matrix, overview_matrix)
            similarity_matrix
            obj3 = Hotel.objects.filter(bed_type=bed_type)
            paginator = Paginator(obj3, 5)
            page_number = request.GET.get('page')
            obj3 = paginator.get_page(page_number)
            arrObject = []
            for item in obj3:
                print(item.hotel_location)
                arrObject.append(item)
            print(len(arrObject))
            return render(request, 'KhachSan/test.html', {'obj': arrObject, 'obj1': obj1})
    else:
        obj4 = Hotel.objects.raw('select * from hotel')
        print(obj4)
        return render(request, 'KhachSan/KhachSan.html', {'obj3': obj4})