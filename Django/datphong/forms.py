from django import forms
from .models import BookingRoom
class BookingRoomForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.post = kwargs.pop('hoten', None)
        self.post = kwargs.pop('phone', None)
        self.post = kwargs.pop('loaiphong', None)
        self.post = kwargs.pop('check_in', None)
        self.post = kwargs.pop('check_out', None)
        super().__init__(*args, **kwargs)
    def save(self, commit = True):
        bookinghotel = super().save(commit = False)
        bookinghotel.author = self.author
        bookinghotel.hoten = self.hoten
        bookinghotel.phone = self.phone
        bookinghotel.loaiphong = self.loaiphong
        bookinghotel.check_in = self.check_in
        bookinghotel.check_out = self.check_out
        bookinghotel.save()
    class Meta:
        model = BookingRoom
        fields = ["hoten", "phone", "loaiphong", "check_in", "check_out"]