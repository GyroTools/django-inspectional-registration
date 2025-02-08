# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from registration.compat import re_path, patterns, include
admin.autodiscover()

urlpatterns = patterns('',
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^registration/', include('registration.urls')),
)
