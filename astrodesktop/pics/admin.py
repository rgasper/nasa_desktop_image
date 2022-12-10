from django import forms
from django.contrib import admin
from pics.models import Picture


class PictureAdmin(admin.ModelAdmin):
    fields = ("id", "img", "name")
    readonly_fields = ("id", "name")
    list_display = ("name",)


admin.site.register(Picture, PictureAdmin)
