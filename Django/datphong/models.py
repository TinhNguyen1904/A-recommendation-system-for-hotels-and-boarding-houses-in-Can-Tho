from django.db import models
from django.conf import settings
# Create your models here.
class BookingRoom(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hoten = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    loaiphong = models.CharField(max_length=20)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()