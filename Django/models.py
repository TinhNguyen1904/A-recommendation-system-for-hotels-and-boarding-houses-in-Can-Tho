# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountEmailaddress(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=254)
    verified = models.IntegerField()
    primary = models.IntegerField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BookRom(models.Model):
    book_id = models.IntegerField(db_column='BOOK_ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='USER_ID')  # Field name made lowercase.
    book_price = models.IntegerField(db_column='BOOK_PRICE', blank=True, null=True)  # Field name made lowercase.
    book_sum_money = models.IntegerField(db_column='BOOK_SUM_MONEY', blank=True, null=True)  # Field name made lowercase.
    book_status = models.IntegerField(db_column='BOOK_STATUS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book_rom'


class DetailBookRoom(models.Model):
    detail_id = models.IntegerField(db_column='DETAIL_ID', primary_key=True)  # Field name made lowercase.
    book = models.ForeignKey(BookRom, models.DO_NOTHING, db_column='BOOK_ID')  # Field name made lowercase.
    hotel = models.ForeignKey('Hotel', models.DO_NOTHING, db_column='HOTEL_ID')  # Field name made lowercase.
    detail_number = models.IntegerField(db_column='DETAIL_NUMBER', blank=True, null=True)  # Field name made lowercase.
    detail_price_free = models.IntegerField(db_column='DETAIL_PRICE_FREE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detail_book_room'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class HomeBooking(models.Model):
    id = models.BigAutoField(primary_key=True)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    room = models.ForeignKey('HomeRoom', models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'home_booking'


class HomeRoom(models.Model):
    id = models.BigAutoField(primary_key=True)
    number = models.IntegerField()
    category = models.CharField(max_length=3)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'home_room'


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

    class Meta:
        managed = False
        db_table = 'hotel'


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

    class Meta:
        managed = False
        db_table = 'motel'


class ReviewsHotel(models.Model):
    cmt_id = models.IntegerField(db_column='CMT_ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='USER_ID')  # Field name made lowercase.
    hotel = models.ForeignKey(Hotel, models.DO_NOTHING, db_column='HOTEL_ID', blank=True, null=True)  # Field name made lowercase.
    cmt_title = models.CharField(db_column='CMT_TITLE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cmd_rating = models.IntegerField(db_column='CMD_RATING', blank=True, null=True)  # Field name made lowercase.
    cmd_content = models.CharField(db_column='CMD_CONTENT', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reviews_hotel'


class ReviewsMotel(models.Model):
    re_id = models.IntegerField(db_column='RE_ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='USER_ID')  # Field name made lowercase.
    motel = models.ForeignKey(Motel, models.DO_NOTHING, db_column='MOTEL_ID')  # Field name made lowercase.
    re_motel_rating1 = models.IntegerField(db_column='RE_MOTEL_RATING1', blank=True, null=True)  # Field name made lowercase.
    re_motel_reviews = models.TextField(db_column='RE_MOTEL_REVIEWS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reviews_motel'


class SocialaccountSocialaccount(models.Model):
    id = models.BigAutoField(primary_key=True)
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    id = models.BigAutoField(primary_key=True)
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)
    key = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    id = models.BigAutoField(primary_key=True)
    socialapp_id = models.BigIntegerField()
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp_id', 'site'),)


class SocialaccountSocialtoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)


class Users(models.Model):
    user_id = models.IntegerField(db_column='USER_ID', primary_key=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    user_email = models.CharField(db_column='USER_EMAIL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    user_pass = models.CharField(db_column='USER_PASS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_phone = models.CharField(db_column='USER_PHONE', max_length=11, blank=True, null=True)  # Field name made lowercase.
    user_address = models.CharField(db_column='USER_ADDRESS', max_length=1024, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'
