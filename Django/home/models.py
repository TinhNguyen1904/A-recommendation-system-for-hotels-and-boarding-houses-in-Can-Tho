from django.db import models
from django.conf import settings
# Create your models here.
class Room(models.Model):
    ROOM_CATEGORIES = (
        ('YAC', 'Phòng tiêu chuẩn giường đôi (Standard Double Room)'),
        ('NAC', 'Phòng tiêu chuẩn 2 giường (Standard Twin Room)	'),
        ('DEL', 'Phòng gia đình (Family Room)'),
    )
    number = models.IntegerField()
    category = models.CharField(max_length=100, choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.number}. {self.category} with {self.beds} beds for {self.capacity} people'

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'


