from adminsortable.admin import SortableStackedInline, SortableAdmin
from django.contrib import admin
from django.utils.translation import ugettext as _

from .models import Services, Service


class ServicesInline(SortableStackedInline):
    extra = 1
    model = Service

class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js', # jquery
        )
class ServicesAdmin(SortableAdmin):
    inlines = [ServicesInline, ]

admin.site.register(Services, ServicesAdmin)