from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^/?', include('test_app.urls',namespace='test')),
    url(r'^', include('cms.urls')),

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
