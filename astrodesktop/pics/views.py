from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from pics.models import Picture


class PictureListView(ListView):
    model = Picture
    context_object_name = "pictures"
