import os

from django.db import models
from PIL import Image

from astrodesktop.models import TimeStampedModel


class Picture(TimeStampedModel):
    img = models.ImageField(height_field="img_height", width_field="img_width")
    thumb = models.ImageField(
        height_field="thumb_height", width_field="thumb_width"
    )  # not using django-thumbnails cus lets keep it KISS
    img_filename = models.TextField()  # corresponds to name property
    thumb_width = models.IntegerField(blank=True, null=True)
    thumb_height = models.IntegerField(blank=True, null=True)
    img_width = models.IntegerField(blank=True, null=True)
    img_height = models.IntegerField(blank=True, null=True)

    def save(self):
        def make_thumbnail(img, img_path) -> str:
            """
            Makes an image thumbnail and saves it right next to the image
            Only will work in the save method
            """
            thumb = Image.open(img)
            thumb.thumbnail((200, 200), Image.ANTIALIAS)
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
