from django.shortcuts import render, get_object_or_404
from django.views import View
# Create your views here.
from .models import Motel, ReviewsMotel, Comment
from dangnhapdangky.models import Users
from .forms import CommentForm
from django.http import HttpResponseRedirect

def noidungnhatro(request, id):
    nhatro = Motel.objects.get(motel_id=id)
    views = ReviewsMotel.objects.filter(motel_id=id)
    views1 = Users.objects.filter( user_id=id)
    cmt = Comment.objects.all()
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST, author=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    print(nhatro)
    context = {"Motel": nhatro, "views":views, "views1":views1, "form":form, "cmt":cmt}
    return render(request, 'noidungnhatro/noidungnhatro.html', context)

# class home(View):
#     def get(self, request):
#         obj = Motel.objects.all()
#         print(obj)
#         return render(request, 'noidungnhatro/noidungnhatro.html', {'obj': obj})



