# Generated by Django 3.2.6 on 2021-10-21 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('hotel_id', models.IntegerField(db_column='HOTEL_ID', primary_key=True, serialize=False)),
                ('hotel_name', models.CharField(blank=True, db_column='HOTEL_NAME', max_length=50, null=True)),
                ('hotel_rating', models.IntegerField(blank=True, db_column='HOTEL_RATING', null=True)),
                ('nunber_rating', models.IntegerField(blank=True, db_column='NUNBER_RATING', null=True)),
                ('title_rating', models.CharField(blank=True, db_column='TITLE_RATING', max_length=50, null=True)),
                ('hotel_price', models.IntegerField(blank=True, db_column='HOTEL_PRICE', null=True)),
                ('hotel_price_free', models.IntegerField(blank=True, db_column='HOTEL_PRICE_FREE', null=True)),
                ('room_type', models.CharField(blank=True, db_column='ROOM_TYPE', max_length=50, null=True)),
                ('hotel_address', models.CharField(blank=True, db_column='HOTEL_ADDRESS', max_length=100, null=True)),
                ('hotel_location', models.CharField(blank=True, db_column='HOTEL_LOCATION', max_length=50, null=True)),
                ('hotel_distance', models.CharField(blank=True, db_column='HOTEL_DISTANCE', max_length=50, null=True)),
                ('hotel_content', models.TextField(blank=True, db_column='HOTEL_CONTENT', null=True)),
                ('number_day', models.CharField(blank=True, db_column='NUMBER_DAY', max_length=50, null=True)),
                ('bed_type', models.CharField(blank=True, db_column='BED_TYPE', max_length=100, null=True)),
                ('hotel_url', models.TextField(blank=True, db_column='HOTEL_URL', null=True)),
                ('hotel_image', models.TextField(blank=True, db_column='HOTEL_IMAGE', null=True)),
            ],
            options={
                'db_table': 'hotel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReviewsHotel',
            fields=[
                ('cmt_id', models.IntegerField(db_column='CMT_ID', primary_key=True, serialize=False)),
                ('cmt_title', models.CharField(blank=True, db_column='CMT_TITLE', max_length=100, null=True)),
                ('cmd_rating', models.IntegerField(blank=True, db_column='CMD_RATING', null=True)),
                ('cmd_content', models.CharField(blank=True, db_column='CMD_CONTENT', max_length=300, null=True)),
            ],
            options={
                'db_table': 'reviews_hotel',
                'managed': False,
            },
        ),
    ]
