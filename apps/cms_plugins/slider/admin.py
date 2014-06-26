from django.contrib import admin

from .models import Slide, Slider


class SlideInline(admin.StackedInline):
    model = Slide
    extra = 1


class SliderAdmin(admin.ModelAdmin):
    inlines = [SlideInline, ]

admin.site.register(Slider, SliderAdmin)