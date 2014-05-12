# -*- coding: utf-8 -*-
from adminsortable.models import Sortable
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _

from cms.models import CMSPlugin
from tinymce.models import HTMLField


class Services(Sortable):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('slider_view', args=[self.pk])

    class Meta(Sortable.Meta):
        verbose_name = _("Services")
        verbose_name_plural = _("All Services")


class Service(Sortable):
    attractions = models.ForeignKey(Services, verbose_name=_("Serives Set"), related_name="services")
    title = models.CharField(_("Title"), max_length=35)
    image = models.ImageField(_(u"Image"), upload_to="media/gallery/images/")
    description = HTMLField(_("Description"), max_length=1024)
    class Meta(Sortable.Meta):
        verbose_name = _("service")
        verbose_name_plural = _("services")

    def __unicode__(self):
        return self.title


class ServicesPlugin(CMSPlugin):
    services = models.ForeignKey(Services)

    def copy_relations(self, oldinstance):
        self.services = oldinstance.services