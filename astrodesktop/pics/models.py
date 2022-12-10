import os

from django.db import models
from PIL import Image

from astrodesktop.models import TimeStampedModel


class Picture(TimeStampedModel):
    img = models.ImageField()
    thumb = models.ImageField()  # not using django-thumbnails cus lets keep it KISS
    img_filename = models.TextField()  # corresponds to name property

    def save(self):
        def make_thumbnail(img, img_path) -> str:
            """
            Makes an image thumbnail and saves it right next to the image
            Only will work in the save method
            """
            thumb = Image.open(img)
            thumb.thumbnail((90, 90), Image.ANTIALIAS)
            dir = os.path.dirname(img_path)
            imgname, imgext = os.path.splitext(self.name)
            thumbname = f"{imgname}_thumb{imgext}"
            imgpath = os.path.join(dir, thumbname)
            thumb.save(imgpath)
            return thumbname

        self.img_filename = self.name
        self.thumb.name = make_thumbnail(self.img, self.img.path)
        super().save()

    @property
    def name(self) -> str:
        return os.path.basename(self.img.name)
