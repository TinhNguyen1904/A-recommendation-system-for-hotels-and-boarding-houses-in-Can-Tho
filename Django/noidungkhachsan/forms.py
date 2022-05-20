from django import forms
from .models import CommentHotel
class CommentFormHotel(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author1', None)
        self.post = kwargs.pop('ratingstar', None)
        super().__init__(*args, **kwargs)
    def save(self, commit = True):
        commenthotel = super().save(commit = False)
        commenthotel.author = self.author
        commenthotel.save()
    class Meta:
        model = CommentHotel
        fields = ["body1","ratingstar"]
