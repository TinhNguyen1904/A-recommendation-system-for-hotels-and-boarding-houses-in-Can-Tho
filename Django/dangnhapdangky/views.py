from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import registerForm, loginForm
from django.contrib.auth import authenticate, login
# Create your views here.
class dangnhapdangky(View):
    def get(self,request):
        rF = registerForm
        return render(request, 'dangnhapdangky/dangky.html', {'rF': rF})

    def post(self,request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        #return HttpResponse('thanh cong')
        return render(request, 'home/index.html')

class loginUser(View):
    def get(self, request):
        lF = loginForm
        return render(request, 'dangnhapdangky/dangnhap.html', {'lF': lF})
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #return HttpResponse('Dang nhap thanh cong')
            return render(request, 'home/index.html')
        else:
            return HttpResponse('Tai khoan khong ton tai')
        #return HttpResponse(password)