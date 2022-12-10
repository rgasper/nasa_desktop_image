import os

from django.db import models

from astrodesktop.models import TimeStampedModel


class Picture(TimeStampedModel):
    img = models.ImageField(null=False)
    img_filename = models.TextField()  # corresponds to name property

    def save(self):
        self.img_filename = self.name
        super().save()

    @property
    def name(self) -> str:
        return os.path.basename(self.img.name)
