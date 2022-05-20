from django import forms

class AvailabilityForm(forms.Form):
    ROOM_CATEGORIES = (
        ('YAC', 'Phòng tiêu chuẩn giường đôi (Standard Double Room)'),
        ('NAC', 'Phòng tiêu chuẩn 2 giường (Standard Twin Room)	'),
        ('DEL', 'Phòng gia đình (Family Room)'),
    )
    room_category = forms.ChoiceField(choices=ROOM_CATEGORIES, required=True)
    check_in = forms.DateTimeField(required=True, input_formats=['%d-%m-%Y',])
    check_out = forms.DateTimeField(required=True, input_formats=['%d-%m-%Y',])