import requests
from cache_memoize import cache_memoize
from django.conf import settings
from django.shortcuts import render
from django.views.generic import ListView
from loguru import logger
from pics.models import Picture


class PictureListView(ListView):
    model = Picture
    context_object_name = "pictures"

    def get_queryset(self):
        queryset = super(PictureListView, self).get_queryset()
        if self.request.GET:
            logger.debug(f"PictureListView Query Params: {self.request.GET}")
            if self.request.GET["order_by"] == "recency":
                queryset = queryset.order_by("-created_on")
            if self.request.GET["order_by"] == "name":
                queryset = queryset.order_by("img")
            if self.request.GET["order_by"] == "width":
                queryset = queryset.order_by("img_width")
            if self.request.GET["order_by"] == "height":
                queryset = queryset.order_by("img_height")
        return queryset


def picture_of_the_day_view(request):
    context = {}
    context["apod_url"] = get_picture_of_the_day_url()
    return render(
        request,
        template_name="pics/pictureoftheday.html",
        context=context,
    )


@cache_memoize(60 * 60 * 4)
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
