# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import ServicesPlugin
from django.utils.translation import ugettext as _

class ServicesCMSPlugin(CMSPluginBase):
    model = ServicesPlugin
    name = _("Services")
    render_template = "services/services.html"

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance.services,
            'services': instance.services.services.all(),
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(ServicesCMSPlugin)
