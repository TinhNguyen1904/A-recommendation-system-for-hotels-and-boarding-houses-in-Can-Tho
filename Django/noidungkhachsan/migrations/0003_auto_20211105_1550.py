# Generated by Django 3.2.6 on 2021-11-05 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noidungkhachsan', '0002_commenthotel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commenthotel',
            old_name='author',
            new_name='author1',
        ),
        migrations.RenameField(
            model_name='commenthotel',
            old_name='body',
            new_name='body1',
        ),
    ]
