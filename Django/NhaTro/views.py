from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from noidungnhatro.models import Motel
from django.views import View
from django.core.paginator import Paginator
# Create your views here.
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


@login_required(login_url='/login/')
def NhaTro(request):
    return render(request, 'NhaTro/NhaTro.html')

def logoutUser(request):
    logout(request)
    return render(request, 'home/index.html')

class home(View):
    def get(self, request):
        obj = Motel.objects.all()
        obj1 = Motel.objects.all()
        paginator = Paginator(obj, 5)
        page_number = request.GET.get('page')
        obj = paginator.get_page(page_number)
        return render(request, 'NhaTro/NhaTro.html', {'obj': obj, 'obj1': obj1})


# class test (View):
#     def get(self, request):
#         obj = Motel.objects.all()
#         return render(request, 'NhaTro.html', {'obj': obj})

# @csrf_exempt
def search(request):
    if request.method=="POST":
        obj1 = Motel.objects.all()
        motel_location = request.POST.get('diadiem')
        if motel_location:
            tfidf = TfidfVectorizer()
            overview_matrix = tfidf.fit_transform(['diadiem'])
            overview_matrix.shape
            similarity_matrix = linear_kernel(overview_matrix, overview_matrix)
            similarity_matrix
            obj3 = Motel.objects.filter(motel_location=motel_location)
            paginator = Paginator(obj3, 5)
            page_number = request.GET.get('page')
            obj3 = paginator.get_page(page_number)
            arrObject = []
            for item in obj3:
                print(item.motel_location)
                arrObject.append(item)
            print(len(arrObject))
            return render(request, 'NhaTro/test.html', {'obj': arrObject, 'obj1': obj1})
        else:
            obj1 = Motel.objects.all()
            motel_price_2 = request.POST.get('mucgia')
            print(motel_price_2)
            tfidf = TfidfVectorizer()
            overview_matrix = tfidf.fit_transform(['mucgia'])
            overview_matrix.shape
            similarity_matrix = linear_kernel(overview_matrix, overview_matrix)
            similarity_matrix
            obj3 = Motel.objects.filter(motel_price_2=motel_price_2)
            paginator = Paginator(obj3, 5)
            page_number = request.GET.get('page')
            obj3 = paginator.get_page(page_number)
            arrObject = []
            for item in obj3:
                print(item.motel_price_2)
                arrObject.append(item)
            print(len(arrObject))
            return render(request, 'NhaTro/test.html', {'obj': arrObject, 'obj1': obj1})
    else:
        obj4 = Motel.objects.raw('select * from motel')
        print(obj4)
        return render(request, 'NhaTro/NhaTro.html', {'obj3': obj4})

def search1(request):
    if request.method=="POST":
        obj1 = Motel.objects.all()
        motel_price = request.POST.get('giacuthe')
        motel_views_2 = request.POST.get('diemdanhgia')
        if motel_views_2:
            tfidf = TfidfVectorizer()
            overview_matrix = tfidf.fit_transform(['diemdanhgia'])
            overview_matrix.shape
            similarity_matrix = linear_kernel(overview_matrix, overview_matrix)
            similarity_matrix
            obj3 = Motel.objects.filter(motel_views_2=motel_views_2)
            paginator = Paginator(obj3, 5)
            page_number = request.GET.get('page')
            obj3 = paginator.get_page(page_number)
            arrObject = []
            for item in obj3:
                print(item.motel_location)
                arrObject.append(item)
            print(len(arrObject))
            return render(request, 'NhaTro/test.html', {'obj': arrObject, 'obj1': obj1})
        else:
            tfidf = TfidfVectorizer()
            overview_matrix = tfidf.fit_transform(['giacuthe'])
            overview_matrix.shape
            similarity_matrix = linear_kernel(overview_matrix, overview_matrix)
            similarity_matrix
            obj3 = Motel.objects.filter(motel_price=motel_price)
            paginator = Paginator(obj3, 5)
            page_number = request.GET.get('page')
            obj3 = paginator.get_page(page_number)
            arrObject = []
            for item in obj3:
                print(item.motel_location)
                arrObject.append(item)
            print(len(arrObject))
            return render(request, 'NhaTro/test.html', {'obj': arrObject, 'obj1': obj1})
    else:
        obj4 = Motel.objects.raw('select * from motel')
        print(obj4)
        return render(request, 'NhaTro/NhaTro.html', {'obj3': obj4})
