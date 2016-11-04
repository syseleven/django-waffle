from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponseNotFound, HttpResponseServerError

import django
print(django.__version__)
from distutils.version import StrictVersion
if StrictVersion(django.__version__) < StrictVersion('1.10'):
    import warnings
    from django.utils.deprecation import RemovedInDjango110Warning
    warnings.filterwarnings(action="ignore", category=RemovedInDjango110Warning)

from test_app import views

handler404 = lambda r: HttpResponseNotFound()
handler500 = lambda r: HttpResponseServerError()

admin.autodiscover()

urlpatterns = [
    url(r'^flag_in_view', views.flag_in_view, name='flag_in_view'),
    url(r'^switch-on', views.switched_view),
    url(r'^switch-off', views.switched_off_view),
    url(r'^flag-on', views.flagged_view),
    url(r'^foo_view', views.foo_view, name='foo_view'),
    url(r'^switched_view_with_valid_redirect',
        views.switched_view_with_valid_redirect),
    url(r'^switched_view_with_valid_url_name',
        views.switched_view_with_valid_url_name),
    url(r'^switched_view_with_invalid_redirect',
        views.switched_view_with_invalid_redirect),
    url(r'^flagged_view_with_valid_redirect',
        views.flagged_view_with_valid_redirect),
    url(r'^flagged_view_with_valid_url_name',
        views.flagged_view_with_valid_url_name),
    url(r'^flagged_view_with_invalid_redirect',
        views.flagged_view_with_invalid_redirect),
    url(r'^flag-off', views.flagged_off_view),
    url(r'^', include('waffle.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
