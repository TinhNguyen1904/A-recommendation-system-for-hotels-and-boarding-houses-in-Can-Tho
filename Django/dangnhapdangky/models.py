from django.db import models


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
