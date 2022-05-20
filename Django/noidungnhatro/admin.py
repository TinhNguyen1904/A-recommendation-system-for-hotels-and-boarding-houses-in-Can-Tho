from django.contrib import admin
from .models import Motel
from .models import ReviewsMotel, Comment

admin.site.register(Motel)
admin.site.register(ReviewsMotel)
admin.site.register(Comment)