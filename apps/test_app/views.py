# -*- coding: utf-8 -*-
from django.template.response import TemplateResponse


def test_view(request):
    context={}
    return TemplateResponse(request,'test.html',context)