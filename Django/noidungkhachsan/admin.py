from django.contrib import admin
from .models import Hotel, ReviewsHotel, CommentHotel
# Register your models here.

admin.site.register(Hotel)
admin.site.register(ReviewsHotel)
admin.site.register(CommentHotel)