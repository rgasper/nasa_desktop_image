from django.urls import path

from . import views

urlpatterns = [path("pictureoftheday/", views.picture_of_the_day_view, name="pictureoftheday")]
