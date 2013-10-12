from django.conf.urls import patterns, include, url

urlpatterns = patterns('test_app.views',
    url(r'^test/?','test_view',name='test_view'),

)
