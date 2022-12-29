from random import choice

from django.http import HttpResponse

# from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import View
from pics.models import Picture


class PictureListView(ListView):
    model = Picture
    context_object_name = "pictures"


class PictureOfTheDayView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(choice(["Hi There", "Hello There", "Well Hello There"]))
