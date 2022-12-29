import requests
from django.conf import settings
from django.shortcuts import render
from django.views.generic import ListView
from pics.models import Picture


class PictureListView(ListView):
    model = Picture
    context_object_name = "pictures"


def picture_of_the_day_view(request):
    context = {}
    context["apod_url"] = get_picture_of_the_day_url()
    return render(
        request,
        template_name="pics/pictureoftheday.html",
        context=context,
    )


def get_picture_of_the_day_url() -> str:
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": settings.NASA_API_KEY,
    }
    response = requests.get(
        url=url,
        params=params,
    )
    if response.status_code == 200:
        return response.json()["url"]
    else:
        raise Exception(f"NASA APOD api failed. Check response for details. {response.content}")
