from django import forms
from pics.models import Picture


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture


# PictureFormSet = forms.modelformset_factory(
# Picture
# )
