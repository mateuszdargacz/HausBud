from adminsortable.admin import SortableStackedInline, SortableAdmin
from django.contrib import admin
from django.utils.translation import ugettext as _

from .models import Services, Service


class ServicesInline(SortableStackedInline):
    model = Service
    extra = 1


class ServicesAdmin(SortableAdmin):
    inlines = [ServicesInline, ]

admin.site.register(Services, ServicesAdmin)