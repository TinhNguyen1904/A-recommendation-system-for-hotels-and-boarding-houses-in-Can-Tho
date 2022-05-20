from django.db import models
from django.conf import settings
from dangnhapdangky.models import Users
# Create your models here.

class Motel(models.Model):
    motel_id = models.IntegerField(db_column='MOTEL_ID', primary_key=True)  # Field name made lowercase.
    motel_name = models.CharField(db_column='MOTEL_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    motel_label = models.CharField(db_column='MOTEL_LABEL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    motel_address = models.CharField(db_column='MOTEL_ADDRESS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    motel_location = models.CharField(db_column='MOTEL_LOCATION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    motel_rating = models.IntegerField(db_column='MOTEL_RATING', blank=True, null=True)  # Field name made lowercase.
    motel_area = models.TextField(db_column='MOTEL_AREA', blank=True, null=True)  # Field name made lowercase.
    motel_price = models.IntegerField(db_column='MOTEL_PRICE', blank=True, null=True)  # Field name made lowercase.
    motel_content = models.TextField(db_column='MOTEL_CONTENT', blank=True, null=True)  # Field name made lowercase.
    motel_views = models.IntegerField(db_column='MOTEL_VIEWS', blank=True, null=True)  # Field name made lowercase.
    motel_image = models.TextField(db_column='MOTEL_IMAGE', blank=True, null=True)  # Field name made lowercase.
    motel_price_2 = models.TextField(db_column='MOTEL_PRICE_2', blank=True, null=True)  # Field name made lowercase.
    motel_views_2 = models.TextField(db_column='MOTEL_VIEWS_2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'motel'

class ReviewsMotel(models.Model):
    re_id = models.IntegerField(db_column='RE_ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey(Users, models.DO_NOTHING, db_column='USER_ID')  # Field name made lowercase.
    motel = models.ForeignKey(Motel, models.DO_NOTHING, db_column='MOTEL_ID')  # Field name made lowercase.
    re_motel_rating1 = models.IntegerField(db_column='RE_MOTEL_RATING1', blank=True, null=True)  # Field name made lowercase.
    re_motel_reviews = models.TextField(db_column='RE_MOTEL_REVIEWS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reviews_motel'

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    star = models.IntegerField(db_column='star')
