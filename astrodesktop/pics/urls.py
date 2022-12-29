from django.urls import path

from . import views

urlpatterns = [path("pictureoftheday/", views.PictureOfTheDayView.as_view(), name="pictureoftheday")]
