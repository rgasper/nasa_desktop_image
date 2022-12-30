from django import forms
from pics.models import Picture

# NOTE unused


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
