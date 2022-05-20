from django.db import models
from dangnhapdangky.models import Users
from django.conf import settings
# Create your models here.

class Hotel(models.Model):
    hotel_id = models.IntegerField(db_column='HOTEL_ID', primary_key=True)  # Field name made lowercase.
    hotel_name = models.CharField(db_column='HOTEL_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hotel_rating = models.IntegerField(db_column='HOTEL_RATING', blank=True, null=True)  # Field name made lowercase.
    nunber_rating = models.IntegerField(db_column='NUNBER_RATING', blank=True, null=True)  # Field name made lowercase.
    title_rating = models.CharField(db_column='TITLE_RATING', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hotel_price = models.IntegerField(db_column='HOTEL_PRICE', blank=True, null=True)  # Field name made lowercase.
    hotel_price_free = models.IntegerField(db_column='HOTEL_PRICE_FREE', blank=True, null=True)  # Field name made lowercase.
    room_type = models.CharField(db_column='ROOM_TYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hotel_address = models.CharField(db_column='HOTEL_ADDRESS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    hotel_location = models.CharField(db_column='HOTEL_LOCATION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hotel_distance = models.CharField(db_column='HOTEL_DISTANCE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hotel_content = models.TextField(db_column='HOTEL_CONTENT', blank=True, null=True)  # Field name made lowercase.
    number_day = models.CharField(db_column='NUMBER_DAY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bed_type = models.CharField(db_column='BED_TYPE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    hotel_url = models.TextField(db_column='HOTEL_URL', blank=True, null=True)  # Field name made lowercase.
    hotel_image = models.TextField(db_column='HOTEL_IMAGE', blank=True, null=True)  # Field name made lowercase.
    hotel_price_2 = models.TextField(db_column='HOTEL_PRICE_2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hotel'

class ReviewsHotel(models.Model):
    cmt_id = models.IntegerField(db_column='CMT_ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey(Users, models.DO_NOTHING, db_column='USER_ID')  # Field name made lowercase.
    hotel = models.ForeignKey(Hotel, models.DO_NOTHING, db_column='HOTEL_ID', blank=True, null=True)  # Field name made lowercase.
    cmt_title = models.CharField(db_column='CMT_TITLE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cmd_rating = models.IntegerField(db_column='CMD_RATING', blank=True, null=True)  # Field name made lowercase.
    cmd_content = models.CharField(db_column='CMD_CONTENT', max_length=300, blank=True, null=True)  # Field name made lowercase.
    hotel_user = models.CharField(db_column='HOTEL_USER', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reviews_hotel'

class CommentHotel(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body1 = models.TextField()
    ratingstar = models.IntegerField(db_column='ratingstar')
