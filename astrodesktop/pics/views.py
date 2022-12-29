from django.shortcuts import render
from django.views.generic import ListView
from pics.models import Picture


class PictureListView(ListView):
    model = Picture
    context_object_name = "pictures"


# class PictureOfTheDayView(TemplateView):

#     template_name = "pics/pictureoftheday.html"

#     def get_context_data(self, request, *args, **kwargs):
#         context = super(PictureOfTheDayView, self).get_context_data(request, **kwargs)
#         context["apod_url"] = "https://apod.nasa.gov/apod/image/2212/M88_2022weebly.jpg"
#         return context


def picture_of_the_day_view(request):
    context = {}
    context["apod_url"] = "https://apod.nasa.gov/apod/image/2212/M88_2022weebly.jpg"
    return render(
        request,
        template_name="pics/pictureoftheday.html",
        context=context,
    )
